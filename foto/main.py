from PIL import Image,ImageFilter
def p1():



    filename = "sobaken.jpg"
    with Image.open(filename) as img:
        img.load()

    img.show()
    width, height = img.size

    format = img.format

    mode = img.mode

    print("Ширина: ", width)
    print("Высота:  ", height)
    print("Формат: ", format)
    print("Цветовая модель:", mode)


def p2():


    i = Image.open('4.jpg')

    i1 = i.reduce(3)
    i1.save('4_1.jpg')

    i2 = i.transpose(Image.FLIP_TOP_BOTTOM)
    i2.save('4_2.jpg')

    i3 = i.transpose(Image.FLIP_LEFT_RIGHT)
    i3.save('4_3.jpg')

def p3():

    for i in range(1, 6):
        k = Image.open(str(i) + '.jpg')
        k = k.filter(ImageFilter.SHARPEN)
        k.save('tftft.jpg')
        k.show()

def p4():

    i = Image.open('watermark.png')
    f = Image.open('1.jpg')

    f.paste(i, (50, 50), i)

    f.save('sobaken.jpg')
    f.show()

p1(), p2(), p3(), p4()