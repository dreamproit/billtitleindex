import os

if os.environ.get('ENVIRONMENT') == "DEV":
    from .dev import *
else:
    from .prod import *