"""

debug_log.py: utility module for printing debug output that can be toggled on or off

"""


from __future__ import print_function

DEBUG = True

def print_debug(*args, **kwargs):
    if DEBUG:
        print("DEBUG:", *args, **kwargs)