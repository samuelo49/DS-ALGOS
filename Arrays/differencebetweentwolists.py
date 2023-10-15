"""
There are various ways in which the difference between two lists can be generated.
Input:
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35] 

Output:
[10, 20, 30, 15]

"""
def findListDifference(lst1, lst2):
    return [num for num in lst1 if num not in lst2]

list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35] 
print(findListDifference(list1, list2)) #[10, 20, 30, 15]