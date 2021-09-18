from deque import Deque


if __name__ == '__main__':
    deque = Deque()
    deque.insert_front(69)
    deque.insert_front(45)
    deque.insert_front(11)

    deque.insert_last(99)
    deque.insert_last(42)

    deque.print_deque(deque.head)

    deque.delete_front()
    deque.delete_last()

    deque.print_deque(deque.head)

    deque.get_front()
    deque.get_last()

    deque.is_present(69)
    deque.is_present(999)
