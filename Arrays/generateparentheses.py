"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3 Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 2 Output: [“()()”, “(())”]

Constraints

1 <= n <= 10,000
"""
def generateParenthesis(n):
    current_string = []
    valid_answers = []

    def recurse(forward_parens_needed, backward_parens_needed):
        nonlocal current_string
        nonlocal valid_answers

        if forward_parens_needed == 0 and backward_parens_needed == 0:
            valid_answers.append("".join(current_string))

        if forward_parens_needed > 0:
            current_string.append("(")
            recurse(forward_parens_needed - 1, backward_parens_needed)
        
        if backward_parens_needed > 0 and backward_parens_needed > forward_parens_needed:
            current_string.append(")")
            recurse(forward_parens_needed, backward_parens_needed - 1)
        if len(current_string) > 0:
            current_string.pop()
    recurse(n, n)
    return valid_answers

print(generateParenthesis(3))