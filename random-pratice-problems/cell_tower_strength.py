
'''
Cell Tower Strength

You are given an array representing the positions of cell towers along a 1-dimensional line. You are given a second array representing customers' positions along the same line. Given these two inputs, you must determine the minimum signal strength *k* such that every customer is covered by at least one cell tower. All cell towers must have the exact same signal strength and cover customers to their left and right equally.

These arrays can be imagined as street addresses along a road. At each address, there might be a customer, and there might also be a tower at that location.
 

EXAMPLE(S)
Let's say cell towers are at: [0, 2, 6, 10]
and customers are at: [0, 5, 11]

In this case, you only need a cell distance of 1, because customer 5 would be covered by 6 and customer 11 would be covered by 10.

If the customers were at: [0, 4, 13], you'd need a distance of 3 in order for customer 13 to be covered by 10.
 

FUNCTION SIGNATURE
def search(customers: list[int], towers: list[int]) -> int:
'''
def search(customers, towers):
    max_so_far = 0
    customer_pointer = 0
    tower_pointer = 0

    while customer_pointer < len(customers):
        def distance_to_current_tower():
            return abs(customers[customer_pointer] - towers[tower_pointer])

        while (tower_pointer < len(towers) - 1
               and abs(customers[customer_pointer] - towers[tower_pointer + 1]) < distance_to_current_tower()):
            tower_pointer += 1

        max_so_far = max(max_so_far, distance_to_current_tower())

        customer_pointer += 1

    return max_so_far