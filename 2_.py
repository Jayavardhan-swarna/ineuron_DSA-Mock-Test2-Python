class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0
    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        carry, value = divmod(x + y + carry, 10)
        curr.next = ListNode(value)
        curr = curr.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if carry > 0:
        curr.next = ListNode(carry)
    return dummy.next

#testing the output
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next

# Output: 7 0 8
