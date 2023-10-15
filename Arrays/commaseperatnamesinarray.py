"""
Given an array of strings, combine them into one string, comma separated except for
the last two pair, which should be separated with the word "and".
We don't want an Oxford comma, so given ["Sam", "Grant", "Jenny"], return "Sam, Grant and Jenny".
console.log(commaSeparate(["Daniel", "Craig"]) == "Daniel and Craig")
console.log(commaSeparate(["Oliver", "Pixel", "Fido"])== "Oliver, Pixel and Fido")
"""


def commaSeparate(input):
    result = []
    for i in range(len(input)):
        if len(input) > 0:
            if i == len(input) - 1:
                result.append(" and ")
            elif len(result) > 0:
                result.append(" , ")
        result.append(input[i])

    return ''.join(result)


print(commaSeparate(["Daniel", "Craig"]))
# print(commaSeparate(["Daniel", "Craig"]) == "Daniel and Craig")
# print(commaSeparate(["Oliver", "Pixel", "Fido"]))