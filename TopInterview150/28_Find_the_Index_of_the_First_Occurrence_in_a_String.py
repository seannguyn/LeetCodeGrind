# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

from typing import Tuple

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        first_occurence_index = -1
        index = 0
        while index < len(haystack):
            if haystack[index] == needle[0]:
                result, matched_characters =  self.potentialMatch(haystack, index, needle)
                if result: return index                
            index += 1

        return -1
    
    def potentialMatch(self, haystack, current_index, needle) -> Tuple[bool, int]:
        next_index = current_index + 1
        matched_characters = 1
        remaining_needle = needle[1:]
        while next_index < len(haystack) and len(remaining_needle) > 0:
            if haystack[next_index] == remaining_needle[0]:
                remaining_needle = remaining_needle[1:]
                next_index += 1
                matched_characters += 1
            else:
                return (False, matched_characters)
        
        return (True if len(remaining_needle) == 0 else False, matched_characters)