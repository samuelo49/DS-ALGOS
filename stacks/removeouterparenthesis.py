"""
Given a valid string s, remove the outermost parentheses of each block
of nested parentheses. E.g. (()()) => ()()
"""


def removeOuterParentheses(s: str) -> str:
    popen, result = 0, []
    for x in s:
        if x == ')':
            popen -= 1
        if popen > 0:
            result.append(x)
        if x == '(':
            popen += 1
    return ''.join(result)

# print(removeOuterParentheses("(()())(())(()(()))"))
print(removeOuterParentheses("()()"))
