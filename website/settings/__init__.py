from .base import *
from .production import *
try:
    from .local import *
except ImportError('Can not import local settings,you must be on production server'):
    pass
