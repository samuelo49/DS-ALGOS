"""
Q. Given a linked list, return the kth element from the end of the list.
   If the k exceeds the length of the list, return -1.
Given a linked list: 13 ➞ 1 ➞ 5 ➞ 3 ➞ 7 ➞ 10, k: 1 // returns 10
Given a linked list: 13 ➞ 1 ➞ 5 ➞ 3 ➞ 7 ➞ 10, k: 7 // returns -1
"""
class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

def kthFromLast(head: ListNode, k: int) -> int:
    if head is None or head.next is None:
        return None
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    if k < len(result):
        return result[len(result) - k]
    return -1

    # if head is None:
    #     return None
    # slow = head
    # fast = head
    # for i in range(k):
    #     if fast is not None:
    #         fast = fast.next
    #     else:
    #         return -1
    # while fast is not None:
    #     fast = fast.next
    #     slow = slow.next
    # return slow.value



# Test Cases
LL1 = ListNode(13, ListNode(1, ListNode(5, ListNode(3, ListNode(7, ListNode(10))))))
print(kthFromLast(LL1, 1)) # 10
print(kthFromLast(LL1, 3)) # 3
print(kthFromLast(LL1, 6)) # 13
print(kthFromLast(LL1, 7)) # -1
print(kthFromLast(None, 7)) # None