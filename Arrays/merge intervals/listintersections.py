"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] 
and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or 
represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Example 1:

Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
"""
def intervals_intersection(interval_list_a, interval_list_b):
    """
    firstList = [[0,2],[5,10],[13,23],[24,25]], 
    secondList = [[1,5],[8,12],[15,24],[25,26]]

    [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    [a, b] -> b is the endpoint of the interval.
    """
    result = []
    i = 0
    j = 0
    while i < len(interval_list_a) and j < len(interval_list_b):
        # lets check if a overlaps b -> interval_list_a intersects interval_list_b
        # lo - the startpoint of the intersection
        # hi - the endpoint of the intersection 
        lo = max(interval_list_a[i][0], interval_list_b[j][0])
        hi = min(interval_list_a[i][1], interval_list_b[j][1])

        if lo <= hi:
            result.append([lo, hi])

        # remove the interval with the smallest endpoint
        if interval_list_a[i][1] < interval_list_b[j][1]:
            i += 1
        else:
            j += 1
    return result
# time complexity: O(M + N) where M and N are the lengths of the two lists.
# space complexity: O(M + N) since we are returning a list of intervals.
# test case 1
interval_list_a = [[0,2],[5,10],[13,23],[24,25]]
interval_list_b = [[1,5],[8,12],[15,24],[25,26]]
print(intervals_intersection(interval_list_a, interval_list_b))


