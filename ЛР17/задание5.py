from PIL import Image, ImageFont, ImageDraw# импорт Image, ImageFont, ImageDraw из PIL

image = Image.open('img/image1_NN.jpg')#Открываем изображение
print('Формат изображения: ',image.format)
print('Размер изображения: ',image.size)
print('Цветовой режим изображения: ',image.mode)#вывод формата размера и цветового режима

img = Image.new('RGBA', (200, 200), 'black')
idraw = ImageDraw.Draw(image)
idraw.rectangle((400, 750, 800, 850), fill='BLACK')#создание прямоугольника черного цвета
#
idraw2 = ImageDraw.Draw(image)
text = "Данишевского Даниила"#текст
font = ImageFont.truetype("arial.ttf", size=18)#шрифт текста
idraw2.text((420, 770), text, font=font)#координаты текста
image.save('img/image5_NN.jpg')#сохраняем изображение
