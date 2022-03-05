from optparse import Option
from typing import Tuple, Dict, List, Optional
from fastapi import FastAPI, Depends, Query
from fastapi.responses import JSONResponse
from elasticsearch_dsl import Q

from btiapp import utils
from btiapp.models import BillBasic, BillStageTitle
from btiapp.documents import BillStageTitleDocument
from btiapp.schemas import BillMatchingTitlesResponse, BillTitlesResponse, BillsTitlesResponse


app = FastAPI()


def parse_list(bills: List[str] = Query(None)):
    """ Parse request query with bill numbers
    
        accepts strings formatted as lists with square brackets
        billnumbers can be in the format
        ["117hr21","116hr2500"], ['117hr21','116hr2500'], [117hr21,116hr2500], [117hr21, 116hr2500], [117hr21] or 117hr21
    """
    def remove_prefix(text: str, prefix: str):
        return text[text.startswith(prefix) and len(prefix):]

    def remove_postfix(text: str, postfix: str):
        if text.endswith(postfix):
            text = text[:-len(postfix)]
        return text

    if bills is None:
        return

    # we already have a list, we can return
    if len(bills) > 1:
        return bills

    # if we don't start with a "[" and end with "]" it's just a normal entry
    flat_names = bills[0]
    if not flat_names.startswith("[") and not flat_names.endswith("]"):
        return bills

    flat_names = remove_prefix(flat_names, "[")
    flat_names = remove_postfix(flat_names, "]")

    names_list = flat_names.split(",")
    
    # remove `"`
    names_list = [remove_prefix(n.strip(), "\"") for n in names_list]
    names_list = [remove_postfix(n.strip(), "\"") for n in names_list]
    
    # remove `'`
    names_list = [remove_prefix(n.strip(), "'") for n in names_list]
    names_list = [remove_postfix(n.strip(), "'") for n in names_list]

    return names_list


def get_bill_titles_by_billnumber(billnumber: str):
    """ Get bill titles and titlesNoYear by billnumber

    Returns:
        tuple
    """
    df = BillStageTitleDocument.search().filter(Q("match", **{"bill_basic.bill_number": billnumber}))
    dfr = df.execute()
    hits_total = dfr.hits.total.value
    bst_data = df[:hits_total].to_queryset().distinct()
    titles = {}
    titlesNoYear = {}
    for bst in bst_data:
        tf = BillStageTitleDocument.search().filter(Q("match_phrase", title=bst.title))
        tfr = tf.execute()
        tf_hits = tfr.hits.total.value
        tf_data = tf[:tf_hits].to_queryset().distinct()
        bills_containing_title = [title.bill_basic.bill_number for title in tf_data]
        
        tnyf = BillStageTitleDocument.search().filter(Q("match_phrase", titleNoYear=bst.titleNoYear))
        tnyfr = tnyf.execute()
        tnyf_hits = tnyfr.hits.total.value
        tnyf_data = tnyf[:tnyf_hits].to_queryset().distinct()
        bills_containing_titleNoYear = [titleNoYear.bill_basic.bill_number for titleNoYear in tnyf_data]
        
        titles[bst.title] = bills_containing_title
        titlesNoYear[bst.titleNoYear] = bills_containing_titleNoYear
    return titles, titlesNoYear


def get_bill_stage_titles_by_billnumber(billnumber: str):
    """ Get bill stage titles by bill number

    Returns:
        tuple
    """
    df = BillStageTitleDocument.search().filter(Q("match", **{"bill_basic.bill_number": billnumber}))
    dfr = df.execute()
    hits_total = dfr.hits.total.value
    bst_data = df[:hits_total].to_queryset().distinct()
    titles = [bst.title for bst in bst_data]
    titlesNoYear = [bst.titleNoYear for bst in bst_data]
    return titles,titlesNoYear
        

@app.get(
    "/bills/titles/{billnumber}",
    response_model=BillTitlesResponse)
def get_bill_titles_by_bill(billnumber: str):
    """Get bill titles by bill number

    Args:
        billnumber (str): bill number

    Returns:
        BillTitlesResponse
    """
    titles, titlesNoYear = get_bill_titles_by_billnumber(billnumber)
    return BillTitlesResponse(titles=titles, titlesNoYear=titlesNoYear)


@app.get(
    "/bills/titles", 
    response_model=BillsTitlesResponse)
def get_bill_titles_by_bills(bills: List[str] = Depends(parse_list)):
    """Get bill titles by billnumber list

    Args:
        bills (List[str], optional): billnumbers list. Defaults to Depends(parse_list).

    Returns:
        BillsTitlesResponse or JSONResponse
    """
    bill_titles = {}
    if bills:
        for bill in bills:
            titles, titlesNoYear = get_bill_titles_by_billnumber(bill)
            bill_titles[bill] = BillTitlesResponse(titles=titles, titlesNoYear=titlesNoYear)
        return BillsTitlesResponse(__root__=bill_titles)
    else:
        return JSONResponse({'Warn': 'Bill numbers list not provided.'}, status_code=400)
        

@app.get(
    "/titles/{title}", 
    response_model=BillMatchingTitlesResponse)
def get_matching_titles(title: str, fuzzy: Optional[bool] = True):
    """Get matching titles

    Args:
        title (str): title that you want to match
        fuzzy (Optional[bool], optional): fuzzy param. Defaults to True.

    Returns:
        BillMatchingTitlesResponse or JSONResponse
    """
    if fuzzy:
        df = BillStageTitleDocument.search().filter(
            Q("match_phrase", title=title) | Q("match_phrase", titleNoYear=title))
        dfr = df.execute()
        hits_total = dfr.hits.total.value
        bst_data = df[:hits_total].to_queryset().distinct()
        titles=[]
        titlesNoYear=[]
        for bst in bst_data:
            titles.append(bst.title)
            titlesNoYear.append(bst.titleNoYear)
        return BillMatchingTitlesResponse(titles=titles, titlesNoYear=titlesNoYear)
    else:
        return JSONResponse({'Warn': 'Can not find fuzzy query parameter'}, status_code=400)


@app.post(
    "/bill/titles/{billnumber}", 
    response_model=BillMatchingTitlesResponse)
def add_new_title_to_bill(billnumber: str, title: str):
    """Add new title to a specific bill dataset

    Args:
        billnumber (str): bill number
        title (str): title that you want to add

    Returns:
        BillMatchingTitlesResponse or JSONResponse
    """
    bill_basic = BillBasic.objects.filter(bill_number=billnumber).first()
    if bill_basic:
        BillStageTitle.objects.get_or_create(bill_basic=bill_basic, title=title, titleNoYear=utils.get_titleNoYear(title))
        titles, titlesNoYear = get_bill_stage_titles_by_billnumber(bill_basic.bill_number)
        return BillMatchingTitlesResponse(titles=titles, titlesNoYear=titlesNoYear)
    else:
        return JSONResponse({'Error': f'Can not find bill depending on this {billnumber}'}, status_code=404)
    
    