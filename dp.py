#!/bin/python
def overlap (dict, b):
    keys = sorted(set(b))
    intervals = []
    for key in keys:
        for val in dict[key]:
            intervals.append([val, key])
    exists = 0
    overlap = 0
    checked = []
    for interval in intervals:
        if interval[0] > overlap:
            if interval[0] <= exists:
                overlap = exists
            exists = interval[1]
            checked.append(interval)
    return len(checked)
            