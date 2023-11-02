# https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            if not s[i].isalnum(): i += 1
            elif not s[j].isalnum(): j -= 1
            else:
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else: return False
        return True

if __name__ == "__main__":
    solution = Solution()