class TextFileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.queue = []

    def read_lines_into_queue(self):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    # Satır sonundaki boşlukları kaldırarak kuyruğa ekliyoruz
                    self.queue.append(line.strip())
        except FileNotFoundError:
            print("Dosya bulunamadı.")

    def process_lines_from_queue(self):
        while self.queue:
            line = self.queue.pop(0)  # Kuyruğun başındaki satırı alıyoruz
            self.process_line(line)

    def process_line(self, line):
        # Burada her satırı işlemek için yapılması gereken işlemleri tanımlayabilirsiniz
        print("İşlenen Satır:", line)


# Kullanım
file_path = "metin_dosyasi.txt"  # İşlem yapılacak metin dosyasının yolu
processor = TextFileProcessor(file_path)

# Dosyadaki satırları kuyruğa ekleyin
processor.read_lines_into_queue()

# Satırları kuyruktan çıkararak işleyin
processor.process_lines_from_queue()
