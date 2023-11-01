# https://leetcode.com/problems/valid-word-square/?envType=study-plan-v2&envId=premium-algo-100

from typing import List

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        if len(words) == 0 or (len(words[0]) != len(words)): return False
        new_words = []

        for i in range(0,len(words[0])):
            new_word = "".join([word[i] for word in words if i < len(word)])
            new_words.append(new_word)

        return new_words == words

if __name__ == "__main__":
    solution = Solution()
    solution.validWordSquare(["abcd","bnrt","crmy","dtye"])

    solution.validWordSquare(["abcd","bnrt","crm","dt"])