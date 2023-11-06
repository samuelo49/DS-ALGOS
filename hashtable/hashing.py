"""
test_list = [1, 2, 3, 2, 1, 1]
Hash / Dictionary in python
    - we create a lookup for easy look up, deleting or updating elements, insertion all happening in 0(1).
    - how to sort in a dictionary?
    - updating 
    - 

    Mostly used for frequency counts
    used in conjunction with other data structures to get to a solution.
    data tracking, its better when grouped together
    graph representation because it offers 0(1) look up when looking up  a node's neighbors

    - need to work on sorting in a dictionary
    - need to work on populating a dictionary
"""
import collections
def populate_dictionary(arr1):
    # need to create a dictionary 
    lookup = {}
    for num in arr1:
        lookup[num] = lookup.get(num, 0) + 1
    return lookup 
test_list = [1, 2, 3, 2, 1, 1]
print(populate_dictionary(test_list))

# do some sorting based on the frequency
def sort_lookup(relationships):
    sorted_relationships = sorted(relationships.items(), key=lambda x: x[1], reverse=True)