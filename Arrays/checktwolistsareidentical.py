"""
This article deals with the task of ways to check if two unordered list contains exact
similar elements in exact similar position,

test_list1 = [1, 2, 4, 3, 5]
test_list2 = [1, 2, 4, 3, 5]
"""

# def twolistsidentical(lst1, lst2):
#     if not lst1 or not lst2: 
#         return False

#     #sort the lists to create identical order
#     lst1.sort()
#     lst2.sort()

#     if lst1 == lst2:
#         return True
#     else:
#         return False

# test_list1 = [1, 2, 4, 3, 5]
# test_list2 = [1, 2, 4, 3, 5]

# print(twolistsidentical(test_list1, test_list2))

# using zip and all()

def twolistsidentical(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    result = all(x==y for x, y in zip(lst1, lst2))
    return result
# test_list1 = [1, 5, 6, 9, 11]
# test_list2 = [3, 4, 7, 8, 10]test_list1 = [1, 2, 4, 3, 5]
test_list1 = [1, 2, 4, 3, 5]
test_list2 = [1, 2, 4, 3, 5]
print(twolistsidentical(test_list1, test_list2))