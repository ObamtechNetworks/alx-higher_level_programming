#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    state = True
    try:
        print("{:d}".format(value))
    except Exception as e:
        state = False
        print("Exception: {}".format(str(e)), file=sys.stderr)
    finally:
        return state
