from PIL import Image
import subprocess

# Открытие изображения
image = Image.open("image1_6.jpg")

# Отображение изображения с помощью внешней программы (например, Фотовьювера на Windows)
image.show()

# Сохранение изображения с измененным форматом
new_filename = "image1_NN.png"
image.save(new_filename)

# Характеристики изображения
format = image.format
size = image.size
mode = image.mode

print("Формат: ", format)
print("Размер: ", size)
print("Цветовой режим: ", mode)