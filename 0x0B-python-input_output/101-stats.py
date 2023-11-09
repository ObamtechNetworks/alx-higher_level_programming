#!/usr/bin/python3
"""This module defines a script that reads from stdin line by line
It computes metrics in this format:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>

For each 10 lines and after a keyboard interruption (CTRL + C),
Statistics since the beginning is printed like this:

Total file size: File size: <total size>

where <total size> is the sum of all previous (see input format above)

Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear, nothing is printed for this status code

format: <status code>: <number>
status codes is printed in ascending order

"""


import sys  # module required to read from stdin
import signal  # required to handle keyboard interruption/signal


def_stat_codes = [200, 301, 400, 401, 403, 404, 405, 500]
stat_codes = {}  # dictionary to keep track fo the status codes/counts
total_size = 0  # variable to keep track of the total file size


# function to print the statistics
def print_stats(signum=None, frame=None):
    """This function prints the stats from the stdin
    It is called every 10 lines and also when keyboard interrupts occurs
    """
    print("File size: {}".format(total_size))
    for stat_code in sorted(stat_codes.keys()):
        print("{}: {}".format(stat_code, stat_codes[stat_code]))


# signal handler for SIGINT (sent by Ctrl+C) it calls, the print_stats func
signal.signal(signal.SIGINT, print_stats)

# loops each line in stdin, parse line and extract status codes/file size
for i, line in enumerate(sys.stdin, 1):
    # splits each line in the stdin in into parts by whitespace
    parts = line.split()

    # check if parts has at least two elements
    if len(parts) >= 2:

        try:
            # cllct second to the last elem in parts, whch is the stat code
            stat_code = int(parts[-2])

            # cllct file size, whch is the last elem in parts, parse to int
            file_size = int(parts[-1])

            # Check if the status code is in the list of default stat codes
            if stat_code in def_stat_codes:
                # this line counts the occurrence of each status code
                stat_codes[stat_code] = stat_codes.get(stat_code, 0) + 1

                # total file size by sum all file size for each line @stdin
                total_size += file_size

                # for every 10 line print stat code
                if i % 10 == 0:
                    print_stats()
        except Exception:
            continue

# call the print_stats() func to print final statistics
print_stats()
