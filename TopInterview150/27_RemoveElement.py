# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = len(nums) - 1
        val_occurences = 0
        
        # important <=
        while(i <= k):
            if nums[i] == val:
                nums[i] = nums[k]
                k -= 1
                val_occurences += 1
            else:
                i += 1
        return len(nums) - val_occurences
        

if __name__ == "__main__":
    
    # this won't work because Solution.merge is not a static method
    # Solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)

    solution = Solution()
    solution.removeElement([0,1,2,2,3,0,4,2], 2)