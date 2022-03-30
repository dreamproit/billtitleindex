import os

if os.environ.get("ENVIRONMENT") == "DEV":
    from billtitleindex.settings.dev import *  # noqa
else:
    from billtitleindex.settings.prod import *  # noqa
