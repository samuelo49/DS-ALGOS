"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""
from collections import deque

def numIslands(grid):
    # need to store visited locations on the grid 
    visited = set()
    # we need a way to track the places we are to explore 
    queue = deque()

    # keep count of number of islands
    num_of_islands = 0

    # helper function to explore the land area
    def bfs(r,c):
        # add the starting point to the queue
        queue.append((r,c))

        # mark this position as visited
        visited.add((r,c))

        # explore the land area
        while queue:
            # get the current position
            row, col = queue.popleft()

            # check the neighbors to see if they are land

            # check the right neighbor
            if col + 1 < len(grid[0]) and grid[row][col + 1] == "1" and (row, col + 1) not in visited:
                queue.append((row, col + 1))
                visited.add((row, col + 1))
            
            # check the left neighbor
            if col - 1 >= 0 and grid[row][col - 1] == "1" and (row, col - 1) not in visited:
                queue.append((row, col - 1))
                visited.add((row, col - 1))

            # check the top neighbor
            if row - 1 >= 0 and grid[row - 1][col] == "1 "and (row - 1, col) not in visited:
                queue.append((row - 1, col))
                visited.add((row - 1, col))
            
            # check the bottom neighbor 
            if row + 1 < len(grid) and grid[row + 1][col] == "1" and (row + 1, col) not in visited:
                queue.append((row + 1, col))
                visited.add((row + 1, col))

            

    # iterate through the grid
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1 and (r,c) not in visited:
                # explore this land area
                bfs(r,c)
                num_of_islands += 1
    return num_of_islands

print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
  