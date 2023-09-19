class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def reverse_queue(queue):
    reversed_queue = Queue()

    while not queue.is_empty():
        item = queue.dequeue()
        reversed_queue.enqueue(item)

    return reversed_queue


# Örnek bir kuyruk oluşturun
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)

# Kuyruğu ters çevirin
reversed_my_queue = reverse_queue(my_queue)

# Ters çevrilmiş kuyruğu yazdırın
while not reversed_my_queue.is_empty():
    print(reversed_my_queue.dequeue())
