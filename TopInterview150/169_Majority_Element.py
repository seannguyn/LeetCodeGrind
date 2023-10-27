# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # ## Build dictionary
        # element_dict = {}
        # max_occurence = -1
        # majority_element = -1
        # for i in range(0, len(nums)):
        #     if nums[i] in element_dict: element_dict[nums[i]] += 1
        #     else: element_dict[nums[i]] = 1

        #     if max_occurence < element_dict[nums[i]]:
        #         max_occurence = element_dict[nums[i]]
        #         majority_element = nums[i]
        # return majority_element

        # ## Boyer-Moore Voting Algorithm
        count = 0
        candidate = None
        for num in nums:
            if count == 0: candidate = num
            count += (1 if candidate == num else -1)
        return candidate

if __name__ == "__main__":

    solution = Solution()
    majority_element = solution.majorityElement([0,0,2,2,2,2,10,10,1,2,10,3,3,4,10,10,10])
    print(majority_element)