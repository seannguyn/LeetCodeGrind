# https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution():
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # # Approach 1: O(n^2)
        # number_of_string = len(strs)
        # prefix = ""
        # prefix_condition = number_of_string - 1
        # j = 0
        # while True:
            
        #     prefix_count = 0
        #     current_character = ""
            
        #     for i in range(0, number_of_string):
        #         if j >= len(strs[i]):
        #             return prefix
                
        #         if current_character == "": 
        #             current_character = strs[i][j]
        #             continue
                
        #         elif current_character == strs[i][j]:
        #             prefix_count += 1

        #     if prefix_count == prefix_condition:
        #         prefix += current_character
        #     else:
        #         return prefix

        #     j += 1
        
        # Approach 2: O(S)
        prefix=[]
        num = len(strs)
        for x in zip(*strs):
            print(f"x: {x}")
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix)

if __name__ == "__main__":
    solution = Solution()
    solution.longestCommonPrefix(["flower","flow","flight"])