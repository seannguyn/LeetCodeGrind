# https://leetcode.com/problems/largest-unique-number/description/?envType=study-plan-v2&envId=premium-algo-100

from collections import Counter
from typing import List

class Solution():
    def largestUniqueNumber(self, nums: List[int]) -> int:
        number_occurences = {}
        current_max = -1
        number_occurrences = Counter(nums)
        for key, value in number_occurrences.items():
            if value == 1 and current_max <= key:
                current_max = key

        return current_max

        # return max([-1] + [k for k,v in Counter(nums).items() if v == 1])

if __name__ == "__main__":
    solution = Solution()
