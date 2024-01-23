'''
❓ PROMPT
Given an array of strings, combine them into one string, comma separated except for the last two pair, which should be separated with the word "and". We don't want an Oxford comma, so given ["Sam", "Grant", "Jenny"], return "Sam, Grant and Jenny".

Example(s)
commaSeparate(["Daniel", "Craig"]) == "Daniel and Craig"
commaSeparate(["Oliver", "Pixel", "Fido"]) == "Oliver, Pixel and Fido"
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function commaSeparate(names) {
def commaSeparate(names: list[str]) -> str:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def commaSeparate(names):
    if len(names) > 1:
        return ', '.join(names[:-1]) + ' and ' + names[-1]
    elif names:
        return names[0]
    else:
        return ''