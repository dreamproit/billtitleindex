import logging
import sys

from btiapp import utils
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = (
        "Run pipeline to load billstatus title data into PostgreSQL DB and index them."
    )

    def add_arguments(self, parser):
        parser.add_argument("--bill_id", nargs="+", type=str)

    def handle(self, *_, **options):
        # configure logging
        print("start run pipeline...")
        if options.get("debug", False):
            log_level = "debug"
        else:
            log_level = options.get("log", "warn")

        if log_level not in ["debug", "info", "warn", "error"]:
            print("Invalid log level (specify: debug, info, warn, error).")
            sys.exit(1)

        if options.get("timestamps", False):
            logging.basicConfig(
                format="%(asctime)s %(message)s", level=log_level.upper()
            )
        else:
            logging.basicConfig(format="%(message)s", level=log_level.upper())

        logFormatter = logging.Formatter(
            "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s"
        )
        rootLogger = logging.getLogger()

        # fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName))
        # fileHandler.setFormatter(logFormatter)
        # rootLogger.addHandler(fileHandler)

        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setFormatter(logFormatter)
        rootLogger.addHandler(consoleHandler)

        bill_id = options.get("bill_id", None)
        if bill_id:
            print("bill_id: {}".format(bill_id))
            to_fetch = bill_id
        elif isinstance(bill_id, str):
            to_fetch = bill_id.split(",")
        else:
            to_fetch = utils.get_json_bills_to_process(options)

            if not to_fetch:
                logging.warn("All bills indexed.")
                return None

            limit = options.get("limit", None)
            if limit:
                to_fetch = to_fetch[: int(limit)]
        return utils.process_set(to_fetch, options)
