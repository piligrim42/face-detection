import cv2
from mtcnn import MTCNN

# Функция для обнаружения лиц

def detect_faces(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    detector = MTCNN() 
    faces = detector.detect_faces(image)
    for face in faces:
        x, y, w, h = face['box']
        # Прямоугольник вокруг лица
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # Заголовок над прямоугольником
        cv2.putText(image, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 1)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    return image

# Старт: любое изображение
image_path = 'test_img.jpg'
result_image = detect_faces(image_path)
cv2.imshow('Result', result_image)
cv2.waitKey(0)



# Тестовый случай 1: обнаружение лица на изображении с человеком, стоящим немного в профиль
image_path = 'test_img1.jpg'
result_image = detect_faces(image_path)
cv2.imshow('Result', result_image)
cv2.waitKey(0)

# Тестовый случай 2: обнаружение лиц на ч/б изображении с несколькими людьми
image_path = 'test_img2.jpg'
result_image = detect_faces(image_path)
cv2.imshow('Result', result_image)
cv2.waitKey(0)

# Тестовый случай 3: обнаружение лиц на изображении с несколькими людьми
image_path = 'test_img3.jpg'
result_image = detect_faces(image_path)
cv2.imshow('Result', result_image)
cv2.waitKey(0)


# Тестовый случай 4: обнаружение лиц на изображении с размытыми лицами в разных позициях
image_path = 'test_img4.jpg'
result_image = detect_faces(image_path)
cv2.imshow('Result', result_image)
cv2.waitKey(0)


print(detect_faces)