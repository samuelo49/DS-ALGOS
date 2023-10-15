"""
Input : 
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
Output :
[9, 10, 4, 5]

Input :
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
Output :
[9, 11, 26, 28]

"""
def intersection(lst1, lst2):
    return [num for num in lst1 if num in lst2]

lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
print(intersection(lst1=lst1, lst2=lst2)) # 0(n) since its one pass, 0(n) for new array


def intersectionwithsets(lst1, lst2):
    return list(set(lst1).intersection(lst2))
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersectionwithsets(lst1=lst1, lst2=lst2)) # 0(n) 0(n)

