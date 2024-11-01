'''
Given a non-negative integer n, find all n-letter words composed by 'a' and 'b', return them in a list of strings in lexicographical order.

Input: 2
Output: ["aa", "ab", "ba", "bb"]

Input: 4
Output: ["aaaa", "aaab", "aaba", "aabb", "abaa", "abab", "abba", "abbb", "baaa", "baab", "baba", "babb", "bbaa", "bbab", "bbba", "bbbb"]
'''
from typing import List

def letter_combination(n):
    def dfs(start_index, path):
        if start_index == n:
            res.append(''.join(path))
            return
        for letter in ['a', 'b']:
            path.append(letter)
            dfs(start_index+1, path)
            path.pop()

    res = []
    dfs(0, [])
    return res