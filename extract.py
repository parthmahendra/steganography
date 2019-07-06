from PIL import Image


def loadImage(location):
    img = Image.open(location).convert("RGB")
    x, y = img.size
    return img, x, y


def binary(i):
    n = 0
    binarr = []
    while 2 ** n <= i:
        n += 1
    for x in range(n - 1, -1, -1):
        if (2 ** x) <= i:
            i -= (2 ** x)
            binarr.append("1")
        else:
            binarr.append("0")
    return "".join(binarr)


def denary(string):
    string = string.lstrip("0")
    t = 0
    for b in range(len(string) - 1, -1, -1):
        t += int(string[len(string) - 1 - b]) * (2 ** b)
    return t


def main():
    usevernam = True
    location = input("Enter file location: ")
    length = int(input("Enter number of characters of hidden text: "))
    vernam_location = input("Enter file location of one-time pad image: ")
    snpixel = int(input("Enter Starting Point of Pixel: "))
    img, width, height = loadImage(location)
    vernam, vwidth, vheight = loadImage(vernam_location)
    bitarray = []
    t = 0
    for y in range(height):
        for x in range(width):
            if (t <= (length * 8) + snpixel - 1):
                r, g, b = img.getpixel((x, y))
                br = binary(r)
                if usevernam:
                    vr, vg, vb = vernam.getpixel((x, y))
                    bvb = binary(vb)
                    bvb = list(bvb)
                    bitarray.append(str(int(list(br)[-1]) ^ int(bvb[-1])) )
                else:
                    bitarray.append(list(br)[-1] )

            t += 1

    t = 0
    binaryarr = []
    for i in range(snpixel, len(bitarray), 8):
        s = ""
        for t in range(8):
            s += bitarray[i + t]
        binaryarr.append(s)

    s = ""
    for b in range(len(binaryarr)):
        binaryarr[b] = chr(denary(binaryarr[b]))
        s += binaryarr[b]
    print(s)


main()
