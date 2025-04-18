# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) < 2:
        return intervals

    intervals.sort()

    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


if __name__ == '__main__':
    print(merge([[1,3],[2,6],[8,10],[15,18]]))
