import math
import os
import random
import re
import sys
from collections import defaultdict



#
# Complete the 'cacheContents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY callLogs as parameter.
#
def get_priority(arr, end_time):
    priority = 0
    arr.sort()
    accessed = [-1]*(end_time+1)
    entered_cache = False
    last_time = 0

    for time in arr:
        if[accessed[time] == -1]:
            accessed[time] = 0
        else:
            accessed[time] += 2

    for idx, t_stamp in enumerate(arr):
        if(idx == 0):
            pass
        elif(t_stamp == last_time):
            pass
        else:
            decay = (t_stamp-last_time-1)
            if(decay>priority):
                priority=0
            else:
                priority -= decay
        priority +=2
        last_time = t_stamp
        if(priority >= 6):
            entered_cache = True
            last_high = t_stamp
            high_priority = priority
            # now just make sure this point stays above 3 until end_time

    if(entered_cache):
        for time in range(last_high, end_time+1):
            if(accessed[time] != -1): # if time is equal to any timestamps after high add that
                high_priority +=2*accessed[time]
            else:
                high_priority -= 1
            if(high_priority <= 3):
                return False
            print("Timestamp: %s and priority: %s "%(time, high_priority))
    # prioity must hit 6
    return entered_cache

def cacheContents(callLogs):
    # create a dict{} of lists
    items_dict = defaultdict(list)
    # return item
    items_cached = []
    
    end_time = 0

    # iterate and add times items accesed to dict
    for sample in callLogs:
        items_dict[str(sample[1])].append(sample[0])
        sample[0] # timestamp
        sample[1] # item

        if(sample[0] > end_time):
            end_time = sample[0]
    # itereate and find cached items
    for item in items_dict:
        if(get_priority(items_dict[item], end_time)):
            items_cached.append(int(item))
    
    return items_cached


if __name__ == '__main__':
    #example array
    arr = [[1,1],[2,1],[3,1],[6,2]]
    print(cacheContents(arr))