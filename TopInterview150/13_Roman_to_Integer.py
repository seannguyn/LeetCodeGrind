# https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        total = 0
        i = 0
        while i < len(s):
            if (s[i] == "I" or \
                    s[i] == "X" or \
                    s[i] == "C"):
                if i+1 < len(s) and f"{s[i]}{s[i+1]}" in symbol_dictionary: 
                    total += symbol_dictionary[f"{s[i]}{s[i+1]}"]
                    i += 2
                else:
                    total += symbol_dictionary[f"{s[i]}"]
                    i += 1
            else:
                total += symbol_dictionary[f"{s[i]}"]
                i += 1
        return total

if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("III"))