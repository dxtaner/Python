import heapq


class CustomQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        # Eklenen öğelerin mutlak değerine göre sıralama
        heapq.heappush(self.queue, abs(item))

    def dequeue(self):
        if not self.is_empty():
            # Mutlak değeri en küçük olanı seç, orijinal değeri ile döndür
            min_value = heapq.heappop(self.queue)
            return min_value
        else:
            print("Kuyruk boş.")
            return None

    def is_empty(self):
        return len(self.queue) == 0


# Özel sıralama kuyruğunu oluşturun
custom_queue = CustomQueue()

# Kuyruğa öğeleri ekleyin (enqueue)
custom_queue.enqueue(3)
custom_queue.enqueue(-5)
custom_queue.enqueue(1)
custom_queue.enqueue(-10)

# Kuyruktan öğeleri çıkarın (dequeue)
while not custom_queue.is_empty():
    item = custom_queue.dequeue()
    if item is not None:
        print("Çıkarılan Öğe:", item)
