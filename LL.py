class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def add_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(data)

    def add_index(self, data, index):
        if self.head is None:
            print("Index doesn't exist")
        else:
            curr = self.head
            while curr.data is not index:
                curr = curr.next
            temp = curr.next
            new_node = Node(data)
            new_node.next = temp
            curr.next = new_node

    def delete_index(self, index):
        if self.head is None:
            print("Index doesn't Exist")
        curr = self.head
        while curr.next.data is not index:
            curr = curr.next
        temp = curr.next
        curr.next = temp.next

    def delete_head(self):
        if self.head is None:
            print("List is empty")
        curr = self.head.next
        self.head = curr

    def reverse(self, head):
        if head.next is None:
            self.head = head
            return
        self.reverse(head.next)
        temp = head.next
        temp.next = head
        head.next = None

    def print(self):
        if self.head is None:
            print("List is Empty")
        curr = self.head
        while curr is not None:
            print(curr.data, end=' -> ')
            curr = curr.next


def main():
    # test cases
    LinkedList = LL()
    LinkedList.add_start(8, )
    LinkedList.add_end(7)
    LinkedList.add_end(3)
    LinkedList.add_end(2)
    LinkedList.add_index(9, 7)
    LinkedList.add_index(12, 3)
    LinkedList.print()
    print()
    LinkedList.reverse(LinkedList.head)
    LinkedList.print()
    print()
    LinkedList.delete_index(3)
    LinkedList.delete_index(12)
    LinkedList.add_end(4)
    LinkedList.print()
    print()
    LinkedList.delete_head()
    LinkedList.print()


if __name__ == "__main__":
    main()
