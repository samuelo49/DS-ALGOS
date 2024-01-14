'''
❓ PROMPT
Businesses like to make phone numbers that have meaning with English characters, but it's hard for users to convert the letter to numbers when dialing. For example,

*1-800-U-B-SMART* becomes *1-800-8-2-76278*

because 8 corresponds to *T, U*, and *V* so the *U* becomes 8, 2 corresponds to *A, B*, and *C* so the *B* becomes 2, and so on according to a phone's dial pad.

Write a function that converts the English letters to their digit equivalent while preserving the formatting.

Example(s)
decodePhoneNumber("1-800-U-B-SMART") == "1-800-8-2-76278"
decodePhoneNumber("1.800.I.C.BUTTS") == "1.800.4.2.28887"
decodePhoneNumber("1-888-GET-RICH") == "1-888-438-7424"
decodePhoneNumber("555-U-HUNGRY!") == "555-8-486479!"


🔎 EXPLORE
State your assumptions & discoveries:


Create examples & test cases:


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O()
Space: O()


📆 PLAN
High-level outline of approach #:


🛠️ IMPLEMENT
function decodePhoneNumber(text) {
def decodePhoneNumber(text: str) -> str:

The dial pad mapping in both directions has been provided for your convenience.

letterToDigit = {
  'A':'2', 'B':'2', 'C':'2',
  'D':'3', 'E':'3', 'F':'3',
  'G':'4', 'H':'4', 'I':'4',
  'J':'5', 'K':'5', 'L':'5',
  'M':'6', 'N':'6', 'O':'6',
  'P':'7', 'Q':'7', 'R':'7', 'S':'7',
  'T':'8', 'U':'8', 'V':'8',
  'W':'9', 'X':'9', 'Y':'9', 'Z':'9',
  }

digitToLetters = {
  '2':['A','B','C'],
  '3':['D','E','F'],
  '4':['G','H','I'],
  '5':['J','K','L'],
  '6':['M','N','O'],
  '7':['P','Q','R','S'],
  '8':['T','U','V'],
  '9':['W','X','Y','Z']
}


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''


def decodePhoneNumber(text: str) -> str:

    letterToDigit = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9',
    }

    decode = []
    for char in text.upper():
        if char in letterToDigit:
            decode.append(letterToDigit[char])
        else:
            decode.append(char)
    return ''.join(decode)

print(decodePhoneNumber("1-800-U-B-SMART") == "1-800-8-2-76278")
print(decodePhoneNumber("1.800.I.C.BUTTS") == "1.800.4.2.28887")
print(decodePhoneNumber("1-888-GET-RICH") == "1-888-438-7424")
print(decodePhoneNumber("555-U-HUNGRY!") == "555-8-486479!")