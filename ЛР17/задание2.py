from PIL import Image#импорт Image из PIL

image = Image.open('img/image1_NN.jpg')#Открываем изображение

rotated = image.rotate(-30)#поворот изображения на 30 градусов по часовой стрелке
rotated.save('img/image2_NN.jpg')#сохраняем изображенгие