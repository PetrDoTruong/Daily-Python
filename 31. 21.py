list1 = [1,2,4]
list2 = [1,3,4] #--> [1,1,2,3,4,4]

head = ListNode()
tail = head

while list1 and list2:
    if list1.val < list2.val:
        tail.next = ListNode(list1.val)
        list1 = list1.next
    else:
        tail.next = ListNode(list2.val)
        list2 = list2.next
    tail = tail.next


while list1:
    tail.next = ListNode(list1.val)
    list1 = list1.next
    tail = tail.next

while list2:
    tail.next = ListNode(list2.val)
    list2 = list2.next
    tail = tail.next

return head.next