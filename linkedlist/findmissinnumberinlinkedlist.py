"""
Given a linked list of sequential, ascending numbers,
return the first missing value or the next value that should be in the list.

let head1 = new Node(1, new Node(3))
let head2 = new Node(-3, new Node(-1))
let head3 = new Node(5, new Node(6, new Node(7, new Node(8, new Node(9)))))
let head4 = new Node(5, new Node(6, new Node(7, new Node(8, new Node(10)))))

console.table([
  findMissing(head1) == 2,
  findMissing(head2) == -2,
  findMissing(head3) == 10,
  findMissing(head4) == 9
])

1->3 => 2
0 => 1
5->6->7->8->9 => 10

"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def findMissing(head: Node) -> int:
    if not head:
        return Node(1, None)

    current = head
    while current and current.next:
        if current.val != current.next.val - 1:
            return current.val + 1
        current = current.next
    return current.val + 1


head1 = Node(5, Node(6, Node(7, Node(8, Node(9)))))

print(findMissing(head1))
