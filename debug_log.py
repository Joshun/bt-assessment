from __future__ import print_function

DEBUG = True

def print_debug(*args, **kwargs):
    if DEBUG:
        print("DEBUG:", *args, **kwargs)