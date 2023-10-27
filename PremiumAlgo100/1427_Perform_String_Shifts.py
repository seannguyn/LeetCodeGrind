# https://leetcode.com/problems/perform-string-shifts/submissions/?envType=study-plan-v2&envId=premium-algo-100

from typing import List, Tuple

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        _, amount = self.compute_final_shift(s, shift)
        return s[-amount:] + s[:-amount]
    
    def compute_final_shift(self, s: str, shift: List[List[int]]) -> Tuple[int, int]:
        final_direction = 1
        final_amount = 0
        s_length = len(s)
        for _shift in shift:
            if _shift[0] == 1: final_amount += _shift[1]
            else: final_amount += s_length - _shift[1]
        return (final_direction, final_amount % s_length)

if __name__ == '__main__':
    s = "abcdefg"
    print(s)
    
    print(s[2:])    # Skip first    2, take the rest
    print(s[-2:])   # Take last     2
    print(s[5:])    # Skip first    5, take the rest

    print(s[:5])    # Take first    5
    print(s[:-4])   # Skip last     4
    print(s[:3])    # Take first    3

    solution = Solution()
    new_s = solution.stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]])


# s[-move:] + s[:-move]

    a = "asdfghjkl;"
    print(a[7:])        # kl;
    print(a[-5:])       # hjkl;
    print(a[:4])        # asdf
    print(a[:-6])       # asdf