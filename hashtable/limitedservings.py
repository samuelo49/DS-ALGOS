"""
You're a bartender, and you have to look out for your patrons - you don't want them to drink too much.
Assume everyone is having the same drink, and everyone has the same set amount of "allowed servings".
Given an array of patrons (denoted by their names, eg: Adrian), and an integer value representing
"allowed servings", return True if someone attempts to go over the allowed number of servings per person.
Otherwise, False if no one drinks too much.
Can you think of any data structures that might help?

['Joe', 'Bart', 'Larry', 'Joe', 'Carl', 'Doug', 'Joe']
allowedServings = 2
returns True because Joe went over the limit.
"""


def limitedServings(patrons, allowedServings) -> bool:
    countServings = {}

    for patron in patrons:
        countServings[patron] = 1 + countServings.get(patron, 0)

    for servings in countServings.values():
        if servings > allowedServings:
            return True
    return False


print(limitedServings(['Joe', 'Bart', 'Larry', 'Joe', 'Carl', 'Doug', 'Joe'], 2))
