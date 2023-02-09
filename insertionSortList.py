# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head.next # the node we want to insert into sorted list

        sudo_sort_head = ListNode(0, head) # sudo head points to the real head
        sort_tail = head

        # We have one lists:
        #   sudo_sort_head (val = 0 ) -> sorted_head -> ... -> sorted_tail -> node (the node we want to sort) -> unsorted nodes -> ... -> None

        while node != None:
            next_unsort_head = node.next
            if node.val > sort_tail.val:
                # Already sorted
                sort_tail = node
            else:
                ptr = sudo_sort_head
                while ptr.next.val < node.val:
                    ptr = ptr.next
                node.next = ptr.next
                ptr.next = node

            node = next_unsort_head
            sort_tail.next = node

        return sudo_sort_head.next

def parse(head: Optional[ListNode]):
    if ListNode == None:
        return []

    ptr = head
    ret = []
    count = 0
    while ptr != None:
        ret.append(ptr.val)
        ptr = ptr.next
    return ret
sol = Solution()

tc1 = ListNode(4)
tc1.next = ListNode(2)
tc1.next.next = ListNode(1)
tc1.next.next.next = ListNode(3)

tc2 = ListNode(-1)
tc2.next = ListNode(5)
tc2.next.next = ListNode(3)
tc2.next.next.next = ListNode(4)
tc2.next.next.next.next = ListNode(0)

tc3 = ListNode(3)
tc3.next = ListNode(3)
tc3.next.next = ListNode(3)
tc3.next.next.next = ListNode(3)

tc4 = ListNode(10)
tc4.next = ListNode(3)

tc5 = ListNode(3)
tc5.next = ListNode(10)

tc6 = ListNode(3)

tc7 = ListNode(3)
tc7.next = ListNode(3)
tc7.next.next = ListNode(4)
tc7.next.next.next = ListNode(4)
tc7.next.next.next.next = ListNode(5)
tc7.next.next.next.next.next = ListNode(5)

tc8 = ListNode(5)
tc8.next = ListNode(5)
tc8.next.next = ListNode(4)
tc8.next.next.next = ListNode(4)
tc8.next.next.next.next = ListNode(3)
tc8.next.next.next.next.next = ListNode(3)


print (parse(sol.insertionSortList(tc1)), [1,2,3,4])
print (parse(sol.insertionSortList(tc2)), [-1,0,3,4,5])
print (parse(sol.insertionSortList(tc3)), [3,3,3,3])
print (parse(sol.insertionSortList(tc4)), [3,10])
print (parse(sol.insertionSortList(tc5)), [3,10])
print (parse(sol.insertionSortList(tc6)), [3])
print (parse(sol.insertionSortList(tc7)), [3,3,4,4,5,5])
print (parse(sol.insertionSortList(tc8)), [3,3,4,4,5,5])
