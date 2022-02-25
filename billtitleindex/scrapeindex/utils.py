import os
import json
import logging
import ciso8601
from datetime import datetime
from congress.tasks import utils as cu
from congress.tasks import bills
from scrapeindex.models import BillBasic, BillTitles, BillStageTitle

def get_config():
    # read in an opt-in config file for changing directories and supplying email settings
    # returns None if it's not there, and this should always be handled gracefully
    path = "config.yml"
    if os.path.exists(path):
        # Don't use a cached config file, just in case, and direct_yaml_load is not yet defined.
        import yaml
        config = yaml.load(open(path), Loader=yaml.BaseLoader)
    else:
        config = None
    
    return config

def get_data_path(*args):
    # Utility function to generate a part of the path
    # to data/{congress}/bills/{billtype}/{billtypenumber}
    # given as many path elements as are provided. args
    # is a list of zero or more of congress, billtype,
    # and billtypenumber (in order).
    args = list(args)
    if len(args) > 0:
        args.insert(1, "bills")
    return os.path.join(cu.data_dir(), *args)
    
def filter_ints(seq):
    for s in seq:
        try:
            yield int(s)
        except:
            # Not an integer
            continue
        

def get_json_bills_to_process(options):
    if not options.get('congress'):
        congresses = sorted(filter_ints(os.listdir(get_data_path())))
    else:
        congresses = sorted([int(c) for c in options['congress'].split(',')])
        
    # walk through congress
    for congress in congresses:
        # turn this back into a string
        congress = str(congress)
        
        # walk through all bill types in that congress
        # (sort by bill type so that we proceed in a stable order each run)
        
        bill_types = [bill_type for bill_type in os.listdir(get_data_path(congress)) if not bill_type.startswith(".")]
        
        for bill_type in sorted(bill_types):
            
            # walk through each bill in that congress and bill type
            # (sort by bill number so that we proceed in a normal order)
            
            bills = [bill for bill in os.listdir(get_data_path(congress, bill_type)) if not bill.startswith(".")]
            
            for bill_type_and_number in sorted(bills, key = lambda x : int(x.replace(bill_type, ""))):
                dp = get_data_path(congress, bill_type, bill_type_and_number, "data.json")
                
                if os.path.exists(dp):
                    # TODO: check if this bill already indexed
                    bill_id = f"{bill_type_and_number}-{congress}"
                    yield bill_id


def process_set(to_fetch, options):
    errors = []
    saved = []
    skips = []
    
    for id in to_fetch:
        try:
            results = process_data_json(id, options)
        except Exception as e:
            if options.get('raise', False):
                raise
            else:
                errors.append((id, e, cu.format_exception(e)))
                continue
            
        if results.get('ok', False):
            if results.get('saved', False):
                saved.append(id)
                logging.info("[%s] Saved" % id)
            else:
                skips.append(id)
                logging.warn("[%s] Skipping: %s" % (id, results['reason']))
        else:
            errors.append((id, results, None))
            logging.error("[%s] Error: %s" % (id, results['reason']))
    
    if len(errors) > 0:
        message = "\nErrors for %s items:\n" % len(errors)
        for id, error, msg in errors:
            message += "\n\n"
            if isinstance(error, Exception):
                message += "[%s] Exception:\n\n" % id
                message += msg
            else:
                message += "[%s] %s" % (id, error)
                
        cu.admin(message)   # email if possible
        
    logging.warning("\nErrors for %s." % len(errors))
    logging.warning("Skipped %s." % len(skips))
    logging.warning("Saved data for %s." % len(saved))
    
    return saved + skips    # all of the OK's


def process_data_json(bill_id, options):
    # Load an existing bill status JSON file.
    data_json_fn = bills.output_for_bill(bill_id, 'json')
    source = cu.read(data_json_fn)
    bill_data = json.loads(source)
    bill_basic = BillBasic.create(
        bill_id=bill_id, 
        bill_type=bill_data['bill_type'],
        number=int(bill_data['number']),
        congress=int(bill_data['congress']),
        introduced_at=datetime.strptime(bill_data['introduced_at'], '%Y-%m-%d').date(),
        updated_at=ciso8601.parse_datetime(bill_data['updated_at'])
    )
