"""
You're given a comma-separated string of names, and you want to print how many times
each name appeared. For each person that appears,
you should print a string {name} appeared {x} times., in order of appearance.
To properly compare results in the test suite, return an array of strings joined
by a newline as the result of your method.

console.log(printNameFreq("Tony, Jessica, Paavo, Jessica, Tony, Zoe") ==
"Tony appeared 2 times.\n\
Jessica appeared 2 times.\n\
Paavo appeared 1 time.\n\
Zoe appeared 1 time.")

console.log(printNameFreq("") == "Nobody appeared.")
"""

def printNameFreq(names):
    countDict = {}
    for name in names.split(","):
        countDict[name] = 1 + countDict.get(name,0)
    result = []
    for key,value in countDict.items():
        name,appearance = key,value
        result.append(f"{name} appeared {appearance} times.")
    return "\n".join(result)


names = "Tony, Jessica, Paavo, Jessica, Tony, Zoe"

print(printNameFreq(names))

