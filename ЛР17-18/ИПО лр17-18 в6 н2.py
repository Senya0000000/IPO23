from PIL import Image

# Открытие изображения
image = Image.open("image1_NN.png")

# Поворот изображения на заданный угол (10-30 градусов по часовой стрелке)
angle = 10
rotated_image = image.rotate(-angle)

# Сохранение повернутого изображения
new_filename = "image2_NN.png"
rotated_image.save(new_filename)

print("Изображение успешно повернуто и сохранено.")