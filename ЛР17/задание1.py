#Исходное изображение хранится в папке "img"
from PIL import Image#импорт Image из PIL

image = Image.open('img/image1_NN.jpg')#Открываем изображение
print('Формат изображения: ',image.format)
print('Размер изображения: ',image.size)
print('Цветовой режим изображения: ',image.mode)#вывод формата размера и цветового режима
