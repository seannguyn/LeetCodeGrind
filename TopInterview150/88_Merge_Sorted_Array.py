# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while(i < m and j < n):
            if nums2[j] <= nums1[i]:
                nums1.insert(i+1, nums2[j])
                j+=1
            i+=1
        print(nums1)
        if j < n:
            nums1 += nums2[j:]
        
        print(nums1)

if __name__ == "__main__":
    
    # this won't work because Solution.merge is not a static method
    # Solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)

    solution = Solution()
    solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)