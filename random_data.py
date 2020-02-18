# Code to generate a sample of random data
import random
import time

def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
     return str_time_prop(start, end, '%Y-%m-%d %H:%M', prop)


samp = open("sample.dat", "w")
for i in range(500):
    plate = random.randint(0000,9999)
    line = str(plate)+" "+random_date("2000-1-1 00:00", "2020-02-17 23:59", random.random())
    print(line, file=samp)
samp.close()
