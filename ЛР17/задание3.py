from PIL import Image#импорт Image из PIL

image = Image.open('img/image1_NN.jpg')#Открываем изображение

cropped = image.crop((85, 440, 570, 820))#Обрезаем изображение
cropped.save('img/image3_NN.jpg')#сохраняем изображение