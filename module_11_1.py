from PIL import Image, ImageFilter

"""Библиотека Pillow предоставляет возможность работы с изображениями.
В коде ниже представлена возможность расширения Python в виде:
1. Вывода параметров изображения;
2. Изменения размера изображения
3. Изменения формата с JPEG на PNG
4. Обработка изображения при помощи модуля ImageFilter
5. Объединения двух изображений в одно"""

small = Image.open('small_silva.jpg')
big = Image.open('big_silva.jpg')

print(small.size, big.size, small.format, big.format, small.mode, big.mode)

big_size = (1280, 960)
big.thumbnail(big_size)

small.save('change_size_small.jpg', 'png')
big.save('change_size_big.jpg', 'png')
change_size_small = Image.open('change_size_small.png')
change_size_big = Image.open('change_size_big.png')

print(change_size_small.size, change_size_big.size,
      change_size_small.format, change_size_big.format,
      change_size_small.mode, change_size_big.mode)

big_silva_filter = big.filter(ImageFilter.DETAIL)
small_silva_filter = small.filter(ImageFilter.SMOOTH_MORE)

img = Image.blend(big_silva_filter, small_silva_filter, 0.6)
img.save('img.jpg')
img.show()
