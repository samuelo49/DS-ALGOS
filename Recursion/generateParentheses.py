"""
Given n pairs of parentheses, 
write a function to generate all combinations of well-formed parentheses.


Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

Explore:
    n = 2
    ["(())","()()"]
"""
def generateParentheses(n):
    result = []
    if n < 1:
        return [""]
    def backtrack(s, left, right):
        #perfect string that has both equal opening and closing parentheses we add to result array
        if len(s) == 2 * n:
            result.append(s)
        
        # if opening '(' are less than n then we call backtrack and increment counter
        if left < n:
            backtrack(s+'(', left + 1, right)

        # if right = closing ')' is less than left = '(' we balance up the string by calling backtrack with a closing ')' and increment right count
        if right < left:
            backtrack(s+')', left, right+1)
    # initialize the recursive call 
    backtrack(s='',left=0,right=0)
    return result

#test case
print('0 ', generateParentheses(n=0))
print('1 pair ', generateParentheses(n=1))
print('2 pairs ',generateParentheses(n=2))
print('3 pairs ',generateParentheses(n=3))
