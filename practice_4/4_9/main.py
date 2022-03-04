# 4.9: "Миниатюра для сайта"
# Для работы данной программы необходимо импортировать
# изображение с названием "image.jpg" в папку 4.9 данного проекта.
from PIL import Image


def make_preview(size, colors):
    img = Image.open("image.jpg")
    img = img.resize(size)
    img = img.quantize(colors)
    img.save('res.bmp')


make_preview((200, 200), 10)
