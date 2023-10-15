"""
Given an integer array flowerbed containing 0's and 1's,
where 0 means empty and 1 means not empty, and an integer
newFlowers, return true if all newFlowers can be planted
in the flowerbed without violating the no-adjacent-flowers rule.
[1,0,0,0,1], n = 1
[0]
"""


def canPlantFlowers(flowerbed, newFlowers) -> bool:
    flowerpot = [0] + flowerbed + [0]

    if newFlowers == 0:
        return True

    for i in range(1,len(flowerpot)-1):
        if flowerpot[i - 1] == 0 and flowerpot[i] == 0 and flowerpot[i+1] == 0:
            flowerpot[i] = 1
            newFlowers -= 1
    return newFlowers <= 0

