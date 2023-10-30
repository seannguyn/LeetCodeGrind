class Solution():
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        first_character_found = False
        for character in reversed(s):
            if character == " " and not first_character_found:
                continue
            elif character == " " and first_character_found:
                return count
            else:
                count += 1
                first_character_found = True
        return count
        
        # # One-line solution 
        # return len(s.split()[-1])

if __name__ == "__main__":
    solution = Solution()
