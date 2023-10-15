"""
Given an array and a target count X, return true if there are less than X distinct values
 in the array. For example, given [1, 2, 2, 3, 3] and 4, return true because there
 are only 3 distinct values 1, 2, and 3.
 [1, 2, 2, 3, 3] and 4  -> 1,2,3==True
 [] -> 1 ==True
 [1,2] -> 2 == False
"""


def fewerThanTargetDistinct(arr, target):
    countDistinctInteger = {}
    for num in arr:
        countDistinctInteger[num] = 1 + countDistinctInteger.get(num, 0)

    if len(countDistinctInteger.keys()) < target:
        return True
    return False

print(fewerThanTargetDistinct([1, 2, 2, 3, 3],4))
