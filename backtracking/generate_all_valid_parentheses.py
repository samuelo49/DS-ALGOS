'''
    Given an integer n, generate all strings with n matching parentheses. "matching" parentheses mean

there is equal number of opening and closing parentheses.
each opening parenthesis has matching closing parentheses.
For example, () is a valid string but )( is not a valid string because ) has no matching parenthesis before it and ( has no matching parenthesis after it.

Input
n: number of matching parentheses
Output
all valid strings with n matching parentheses

Examples
Example 1:
Input:

n = 2
Output: (()) ()()

Explanation:

There are two ways to create a string with 2 matching parentheses.

Example 2:
Input:

n = 3
Output: ((())) (()()) (())() ()(()) ()()()

Explanation:

There are 5 ways to create a string with 3 matching parentheses.
'''
def generate_parentheses(n):
    def dfs(start_index, path, open_count, close_count, res):
        if start_index == 2 * n:
            res.append(''.join(path))
            return 
        if open_count < n:
            path.append('(')
            dfs(start_index + 1, path, open_count + 1, close_count, res)
            path.pop()
        if close_count < open_count:
            path.append(')')
            dfs(start_index + 1, path, open_count, close_count + 1, res)
            path.pop()
    ans = []
    dfs(0, [], 0,0, ans)
    return ans
