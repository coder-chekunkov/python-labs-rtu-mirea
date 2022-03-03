# 4.6: "Шахматная доска"
from PIL import Image, ImageDraw


def board(num, size):
    img = Image.new("RGB", (num * size, num * size), (256, 256, 256))
    draw = ImageDraw.Draw(img)
    color = (0, 0, 0)
    for i in range(num):
        for j in range(num):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                draw.rectangle([j * size, i * size, j * size + size - 1, i * size + size - 1], color)
    img.save('res.png', 'PNG')


board(12, 10)
