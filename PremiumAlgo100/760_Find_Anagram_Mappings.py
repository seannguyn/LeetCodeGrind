# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # walkthrough nums 2 array
        nums2_dict = {}
        for i in range(0, len(nums2)):
            if nums2[i] in nums2_dict: nums2_dict[nums2[i]].append(i)
            else: nums2_dict[nums2[i]] = [i]

        # build anagram mappings
        anagram_mappings = []
        for i in range(0, len(nums1)):
            index_mapping = nums2_dict[nums1[i]].pop(0)
            anagram_mappings.append(index_mapping)
        
        return anagram_mappings

if __name__ == "__main__":

    solution = Solution()
    anagram_mappings = solution.anagramMappings([12,28,46,32,50], [50,12,32,46,28])
    print(anagram_mappings)