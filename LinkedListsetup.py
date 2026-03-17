class LinkedList():
    def __init__(self):
        self.head = None

    def InsertNode(self, element):
        newNode = ListNode(element) 
        if self.head is None:
            self.head = newNode
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = newNode #shuffles node to back


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None



test = LinkedList()
test.InsertNode("3")
test.InsertNode("F")

