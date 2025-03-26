# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
# represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted
# in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.
from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

    merged = []
    inserted = False

    for interval in intervals:
        if interval[1] < newInterval[0]:
            merged.append(interval)
        elif interval[0] > newInterval[1]:
            if not inserted:
                merged.append(newInterval)
                inserted = True
            merged.append(interval)

        else:
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(interval[1], newInterval[1])

    if not inserted:
        merged.append(newInterval)

    return merged

