from PIL import Image

# Открытие изображения
image = Image.open("image2_NN.png")

# Определение размеров изображения
width, height = image.size

# Определение области обрезки (в данном случае - оставляем центральный квадрат)
left = (width - min(width, height)) // 2
top = (height - min(width, height)) // 2
right = left + min(width, height)
bottom = top + min(width, height)
crop_area = (left, top, right, bottom)

# Обрезка изображения
cropped_image = image.crop(crop_area)

# Сохранение обрезанного изображения
new_filename = "image3_NN.png"
cropped_image.save(new_filename)

print("Изображение успешно обрезано и сохранено.")