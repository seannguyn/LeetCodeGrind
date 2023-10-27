# https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/description/?envType=study-plan-v2&envId=premium-algo-100

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        m_pointer = head
        current_m_walk = 1

        n_pointer = None
        current_n_walk = 0
        
        while m_pointer != None:
            if current_m_walk == m:
                n_pointer = m_pointer
                while(n_pointer != None and current_n_walk <= n):
                    n_pointer = n_pointer.next
                    current_n_walk += 1
                m_pointer.next = n_pointer
                
                current_m_walk = 1
                current_n_walk = 0
            else:
                current_m_walk += 1
            m_pointer = m_pointer.next

        return head
        

if __name__ == "__main__":

    solution = Solution()
    # solution.deleteNodes(... ,3 ,2)