from PIL import Image, ImageDraw, ImageFont

image_path = "image1_NN.jpg"  # Путь к изображению
output_path = "image5_NN.jpg"  # Путь для сохранения результата

# Загрузка изображения
image = Image.open(image_path)

# Создание объекта для рисования на изображении
draw = ImageDraw.Draw(image)

# Задание параметров надписи
text = "Емельянович Арсений "
font_size = 20
font = ImageFont.truetype("Arial.ttf", font_size)

# Определение размеров надписи
text_width, text_height = draw.textsize(text, font)

# Задание координат левого верхнего угла прямоугольника
x = 10
y = 10

# Задание размеров прямоугольника
rectangle_width = text_width + 10
rectangle_height = text_height + 10

# Рисование прямоугольника
draw.rectangle([(x, y), (x + rectangle_width, y + rectangle_height)], fill="white")

# Рисование надписи в прямоугольнике
draw.text((x + 5, y + 5), text, fill="black", font=font)

# Сохранение изображения
image.save(output_path)