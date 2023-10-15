"""
Combining two sorted lists
test_list1 = [1, 5, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]
- should we do it in place or create a different array
"""

def combineSortedListsInPlace(lst1, lst2):
    a = len(lst1)
    b = len(lst2)
    i = 0
    j = 0

    result = []
    while i < a and j < b:
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    return result + lst1[i:] + lst2[j:]

test_list1 = [1, 5, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]
print(combineSortedListsInPlace(test_list1, test_list2))



