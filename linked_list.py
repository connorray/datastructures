class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        # O(i) time complexity for the index of the new value
        if not self.head:
            self.head = ListNode(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)

    def delete(self, index):
        # O(i) time complexity for the index of the new value
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        curr = self.head
        for i in range(index - 1):
            if curr.next is None:
                return  # Index out of range
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
