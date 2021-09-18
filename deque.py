from node import Node


class Deque:

    def __init__(self):
        self.head = None

    def insert_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_last(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
        return

    def get_front(self):
        print("Front element is:", self.head.data)
        print()
        return self.head.data

    def get_last(self):
        last = self.head
        while last.next:
            last = last.next
        print("Last element is:", last.data)
        print()
        return last.data

    def delete_front(self):
        self.head = self.head.next

    def delete_last(self):
        last = self.head
        while last.next:
            last = last.next
        last.prev.next = None

    def is_present(self, data):
        last = self.head
        while last.next:
            if last.data == data:
                print(f"Element {data} is present in the deque")
                return
            last = last.next
        print(f"Element {data} is not present in the deque")
        return

    def deque_to_list(self):
        output = list()
        node = self.head
        while node is not None:
            output.append(node.data)
            node = node.next
        return output

    @staticmethod
    def print_deque(node):
        print("\nTraversal")
        while node:
            print(node.data, end=" ")
            node = node.next
        print()
