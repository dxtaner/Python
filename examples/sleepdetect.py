import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import time

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        continue

    bbox, label, conf = cv.detect_common_objects(frame)

    for i in range(len(label)):
        if label[i] == "face":
            x, y, w, h = bbox[i]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Yüz bölgesini griye çevir
            roi_gray = cv2.cvtColor(
                frame[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY)
            eyes = cv.detect_face(roi_gray)

            # Eğer gözler tespit edilmezse ve belirli bir süre boyunca göz tespit edilmezse
            if not eyes:
                t = 0
                while not eyes:
                    t += 1
                    if t > 5:
                        # Sürücü uykuda gibi görünüyor, metin ekleyin
                        cv2.putText(frame, "Surucu Uykuda!", (x, y - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                        time.sleep(2)
                        break

    # Çerçeve içindeki tüm işlemleri tamamladığımızdan emin olmak için bir kopyasını oluşturuyoruz.
    frame_copy = frame.copy()

    # Orjinal çerçeveyi görüntülüyoruz
    cv2.imshow('Kamera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
