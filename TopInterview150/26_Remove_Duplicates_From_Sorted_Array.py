# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     unique_element = 0
    #     dictionary_element = {}
    #     for i in range(0, len(nums)):
    #         if nums[i] in dictionary_element:
    #             dictionary_element[nums[i]]['counter'] += 1
    #         else:
    #             unique_element += 1
    #             dictionary_element[nums[i]] = {
    #                 'counter': 1,
    #                 'index': i
    #             }

    #     for i in range(0, unique_element-1):
    #         next_unique_occurence = dictionary_element[nums[i]]['index'] + dictionary_element[nums[i]]['counter']
    #         nums[i+1] = nums[next_unique_occurence]
    #         i += 1
    #     return unique_element
    
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates = 0
        for i in range(1, len(nums)):
            if(nums[i] == nums[i-1]): duplicates+=1
            else: nums[i-duplicates] = nums[i]
        return len(nums)-duplicates
        

if __name__ == "__main__":

    solution = Solution()
    solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])