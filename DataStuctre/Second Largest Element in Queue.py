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


def find_second_largest(queue):
    if queue.is_empty() or queue.size() < 2:
        return None

    max_element = float('-inf')
    second_max_element = float('-inf')

    while not queue.is_empty():
        item = queue.dequeue()
        if item > max_element:
            second_max_element = max_element
            max_element = item
        elif item > second_max_element and item < max_element:
            second_max_element = item

    return second_max_element


# Örnek bir kuyruk oluşturun
my_queue = Queue()
my_queue.enqueue(3)
my_queue.enqueue(8)
my_queue.enqueue(2)
my_queue.enqueue(10)
my_queue.enqueue(5)

# İkinci en büyük elemanı bulun
second_largest = find_second_largest(my_queue)

if second_largest is not None:
    print("İkinci En Büyük Eleman:", second_largest)
else:
    print("İkinci en büyük eleman bulunamadı.")
