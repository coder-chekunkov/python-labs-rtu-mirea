# 4.9: "Миниатюра для сайта"
from PIL import Image


def make_preview(size, colors):
    img = Image.open("image.jpg")
    img = img.resize(size)
    img = img.quantize(colors)
    img.save('res.bmp')


make_preview((200, 200), 10)
