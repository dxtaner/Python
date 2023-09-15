class CustomerServiceQueue:
    def __init__(self):
        self.queue = []

    def enqueue_customer(self, customer):
        self.queue.append(customer)
        print(f"{customer} müşteri hizmeti kuyruğuna eklendi.")

    def dequeue_customer(self):
        if not self.is_empty():
            customer = self.queue.pop(0)
            print(f"{customer} müşteri hizmeti sırasından çıkarıldı.")
            return customer
        else:
            print("Kuyruk boş, hizmet bekleyen müşteri yok.")
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def customer_count(self):
        return len(self.queue)


# Müşteri hizmeti kuyruğu oluşturma
customer_service = CustomerServiceQueue()

# Müşterileri kuyruğa eklemek (enqueue)
customer_service.enqueue_customer("Müşteri 1")
customer_service.enqueue_customer("Müşteri 2")
customer_service.enqueue_customer("Müşteri 3")

# Kuyruktan müşteri çıkarmak (dequeue)
served_customer = customer_service.dequeue_customer()
if served_customer:
    print(f"{served_customer} müşteriye hizmet veriliyor.")

# Kuyruğun güncel durumunu kontrol etmek
print("Müşteri Sayısı:", customer_service.customer_count())
