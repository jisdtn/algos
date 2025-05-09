# Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
#
# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.
from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:

    if len(intervals) <= 1:
        return 0

    intervals.sort(key=lambda x: x[1]) # сортируем список интервалов intervals по второму элементу каждого интервала, то есть по end.

    count = 0
    prev_end = float('-inf')

    for start, end in intervals:
        if start >= prev_end:
            prev_end = end
        else:
            count +=1
    return count


if __name__ == '__main__':
    print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
