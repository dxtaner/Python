class Stack:
    def __init__(self):
        self.items = []

    # Yığının en üstüne öğe eklemek (push)
    def push(self, item):
        self.items.append(item)

    # Yığının en üstündeki öğeyi çıkarmak (pop)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    # Yığının en üstündeki öğeyi gözlemlemek (peek)
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    # Yığının boş olup olmadığını kontrol etmek
    def is_empty(self):
        return len(self.items) == 0

    # Yığının boyutunu almak
    def size(self):
        return len(self.items)

    # Yığını temizlemek (tüm öğeleri kaldırmak)
    def clear(self):
        self.items = []


# Yığın örneği oluşturalım
my_stack = Stack()

# Bazı öğeleri yığına ekleyelim
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# Yığının boyutunu ve en üstündeki öğeyi görelim
print("Yığının Boyutu:", my_stack.size())
print("En Üstteki Öğe:", my_stack.peek())

# Yığından öğeleri çıkaralım
print("Çıkarılan Öğe:", my_stack.pop())
print("Yığının Boyutu:", my_stack.size())

# Yığını temizleyelim
my_stack.clear()
print("Yığın Temizlendi, Yığın Boş mu?", my_stack.is_empty())
