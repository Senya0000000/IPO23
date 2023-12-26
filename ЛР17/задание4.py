from PIL import ImageFilter, Image#импорт ImageFilter, Image из PIL

image = Image.open('img/image3_NN.jpg')#открываем изображение из 3 задания

blurred = image.filter(ImageFilter.BLUR)
blurred.save('img/image4_NN.jpg')#Фильтр блюр + сохранение изображения

contour = image.filter(ImageFilter.CONTOUR)
contour.save('img/image4_1_NN.jpg')#Фильтр контур + сохранение изображения

detail = image.filter(ImageFilter.DETAIL)
detail.save('img/image4_2_NN.jpg')#Фильтр детали + сохранение изображения
