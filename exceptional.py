import sys
from math import log

def convert(s):
    try:
        return int(s)
    except (ValueError,TypeError) as e:
        print('conversion error: {}'.format(str(e)),file=sys.stderr)
        raise  # re-raise the currently handled exception
		
def string_log(s):
    v = convert(s)
    return log(v)