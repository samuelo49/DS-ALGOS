"""
How to remove an item from the List in Python
Input: ['Rose',' Lily', 'Lotus', 'Sun', 'Sunflower']
item_delete = 'Sun'
Output: ['Rose',' Lily', 'Lotus', 'Sunflower']
"""

def removeItem(lst, item):
    if item not in lst:
        return lst
    lst.remove(item)
    return lst 
lst1 = ['Rose',' Lily', 'Lotus', 'Sun', 'Sunflower']
item1 = 'Sun'
print(removeItem(lst=lst1, item=item1))

