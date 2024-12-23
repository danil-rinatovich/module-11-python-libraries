from PIL import Image, ImageFilter

"""Библиотека Pillow предоставляет возможность работы с изображениями.
В коде ниже представлена возможность расширения Python в виде:
1. Вывода параметров изображения;
2. Изменения размера изображения
3. Изменения формата с JPEG на PNG
4. Обработка изображения при помощи модуля ImageFilter
5. Объединение изображений в одно"""

small = Image.open('small_silva.jpg')
big = Image.open('big_silva.jpg')

print(small.size, big.size, small.format, big.format, small.mode, big.mode)

big_size = (1280, 960)
big.thumbnail(big_size)

small.save('change_format_small.png')
big.save('change_format_big.png')

change_format_small = Image.open('change_format_small.png')
change_format_big = Image.open('change_format_big.png')

print(change_format_small.size, change_format_big.size,
      change_format_small.format, change_format_big.format,
      change_format_small.mode, change_format_big.mode)

small_silva_filter = small.filter(ImageFilter.SMOOTH_MORE)
big_silva_filter = big.filter(ImageFilter.DETAIL)

img = Image.blend(big_silva_filter, small_silva_filter, 0.6)
img.save('img.jpg')
img.show()
