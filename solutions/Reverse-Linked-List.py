# Definition for singly-linked list.
from typing import Optional
from utils import linked_list_to_list, list_to_linked_list, ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


if __name__ == '__main__':
    input_list = [1,2,3,4,5]
    head = list_to_linked_list(input_list)
    reversed_head = Solution().reverseList(head)
    print(linked_list_to_list(reversed_head))
