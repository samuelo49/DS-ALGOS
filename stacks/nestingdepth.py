"""
Many teams use a type of tool called a linter to scan code to ensure it follows
certain standards and best practices. One common rule a linter might check for
is the depth of nesting of control flow. Functions with many levels of nesting
are often overly complex, hard to read or modify, and can be bug farms.
We're going to write a function to determine the depth of control flow
for if-statements so that teams will be automatically notified if it gets too deep.
In Visual Basic (an old language I hope most of you never need to use),
if statements are bounded by four keywords: if, elseif, else, and endif.
Given a sequence of these keywords, return the max nesting depth or -1 if
the structure is incorrect.
The structure is incorrect when:
    The first keyword is anything other than an if.
    If and endif keywords do not pair up or are out of order.
    An else or elseif is not inside an if.
    There are two else blocks in a row.
    An elseif follows an else at a given level.
Start by implementing this with only if, and endif. Then add support for else.
Once that is working, modify the code to support elseif as well.

"""


def vbNesting(controlFlow):
    stack = []
    maxDepth = 0
    for i in range(len(controlFlow)):
        nextWord = controlFlow[i]
        if nextWord == "if":
            stack.append("if")
            maxDepth = max(maxDepth,len(stack))
        elif controlFlow[i] == "endif":
            if len(stack) > 0:
                stack.pop()
            else:
                return -1
        elif nextWord == "elif" or nextWord == "else":
            topKeyword = stack.pop()
            if topKeyword == "if" or topKeyword == "elif":
                stack.append(nextWord)
        else:
            return -1
        if len(stack) == 0:
            return maxDepth
    return -1


print(vbNesting(["if"]) == -1)
print(vbNesting(["endif"]) == -1)
print(vbNesting(["if", "endif"]) == 1)
print(vbNesting(["if", "else", "endif"]) == 1)
print(vbNesting(["if", "endif", "if", "endif"]) == 1)
print(vbNesting(["if", "if", "endif", "endif"]) == 2)
print(vbNesting(["if", "if", "if", "endif", "endif", "endif"]) == 3)
print(vbNesting(["if", "if", "if", "endif", "endif", "if", "endif", "endif"]) == 3)