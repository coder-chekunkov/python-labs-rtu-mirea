# 4.5: "Градиент"
from PIL import ImageDraw
from PIL import Image


def gradient(color):
    new_image = Image.new("RGB", (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    r = 0
    g = 0
    b = 0
    for i in range(new_image.size[0]):
        draw.line((i, 0, i, 512), fill=(r, g, b), width=2)
        if i % 4 == 0:
            if color == "R":
                r += 2
            elif color == "G":
                g += 2
            else:
                b += 2
    new_image.save("res.png", "PNG")


gradient("G")
