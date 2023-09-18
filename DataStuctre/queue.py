class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Kuyruk boş."

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Kuyruk oluşturma
my_queue = Queue()

# Kuyruğa elemanlar eklemek (enqueue)
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

# Kuyruğun boyutunu kontrol etmek
print("Kuyruğun Boyutu:", my_queue.size())

# Kuyruktan elemanları çıkarmak (dequeue)
print("Dequeue:", my_queue.dequeue())
print("Dequeue:", my_queue.dequeue())

# Kuyruğun güncel boyutunu kontrol etmek
print("Güncel Boyut:", my_queue.size())

# Kuyruğun başındaki elemana bakmak (front)
print("Front:", my_queue.items[0]
      if not my_queue.is_empty() else "Kuyruk boş.")
