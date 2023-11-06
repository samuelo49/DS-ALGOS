'''
❓ PROMPT
Given an array of integers representing piles of rocks (e.g., *3* means *3 rocks*), modify the input array to rank the piles from 1 to N, representing the relative sizes of each pile of rocks from smallest to largest.

That is, the pile with the lowest count of rocks should be ranked *1*, the second lowest should be *2*, and so on.

You may use built-in functions provided by your programming language.

Example(s)
Input: [3, 4, 1]  = 3:0, 4:1, 1:2
ranks{3 : 0
4 : 1
1 : 2}

3,4,1 ->     1,3,4
idx = ranks[1] 2
idx = ranks[3] 0
idx = ranks[4] 1

 piles[2] => 1
 piles[0] => 2
 piles[1] => 3
Output: [2, 3, 1]
Explanation: The last index has the smallest pile with 1 rock, so it's ranked 1st place. The first index has the 2nd smallest pile with 3 rocks, so it's ranked 2nd place. The middle index has the 3rd smallest pile with 4 rocks, so it's ranked 3rd place.

Input: [80, 27, 55, 30, 15, 90, 10]
Output: [6, 3, 5, 4, 2, 7, 1]
Explanation:
80 -> 6
27 -> 3
55 -> 5
30 -> 4
15 -> 2
90 -> 7
10 -> 1
The last index has the smallest pile with 1 rock, so it's ranked 1st place. The 2nd smallest pile has 15 rocks, so it's ranked 2nd place. The 3rd smallest pile has 27 rocks, so it's ranked 3rd place. So on and so forth until the 7th smallest pile has 90 rocks, so it's ranked 7th place.

Input: [2, 1]
Output: [2, 1]


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
function rankPiles(piles) {
def rankPiles(piles: list[int]) -> list[int]:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

1,3,4
'''


def rankPiles(piles):
    ranks = {}
    for i in range(len(piles)):
        rockSize = piles[i]
        ranks[rockSize] = i

    rockAmounts = ranks.keys()
    sortedAmount = sorted(rockAmounts)
    print(sortedAmount)
    rank = 1
    for rockAmount in sortedAmount:
        idx = ranks[rockAmount]
        piles[idx] = rank
        rank += 1
    return piles
print(rankPiles([3, 4, 1]))