from __future__ import print_function

import datetime
import time


def print_with_time(content="", nl=0, iter=0):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

    if nl == 1:
        print(st + ">")
    else:
        print(st + ">", end=" ")

    if iter == 0:
        print(content)
    else:
        for val in content:
            print(val)

    print()


def date_to_string(year, month, day, hours=0, minutes=0, seconds=0):
    return '\'' + str(datetime.datetime(year, month, day, hours, minutes, seconds)) + '\''
