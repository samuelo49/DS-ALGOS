"""
how to Flatten a List of Lists in python
Input : l = [1, 2, [3, 4, [5, 6] ], 7, 8, [9, [10] ] ]
Output : l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

def flattenList(lst):
    flat_list = []
    for ele in lst:
        if isinstance(ele, list):
            flat_list.extend(flattenList(ele))
        else:
            flat_list.append(ele)
    return flat_list
test_list = [1, 2, [3, 4, [5, 6] ], 7, 8, [9, [10] ] ]
print(flattenList(test_list))