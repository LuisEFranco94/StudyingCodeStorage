from libs.operations import operator

print("mylib.py:", __name__)

# -- Can't do relative imports from file with parent package

from .operations import operator