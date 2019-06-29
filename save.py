from PIL import Image
import numpy as np


def declareArray(h, w, integer):
    arr = []
    char = 0 if integer else ""
    for y in range(h):
        arr.append([])
        for x in range(w):
            arr[y].append(char)
    return arr


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
    string = string.strip("0")
    t = 0
    for b in range(len(string) - 1, -1, -1):
        t += int(string[b]) * (2 ** b)
    return t


def loadImage(location):
    img = Image.open(location).convert("RGB")
    x, y = img.size
    return img, x, y


def combineBits(arr):
    return list("".join(arr))


def standardiseLength(arr, character, length):
    standardisedarr = []
    for i in arr:
        standardisedarr.append(((length - len(i)) * "0") + i)
    return standardisedarr


def flattenArr(arr):
    outputarr = []
    for i in arr:
        for px in i:
            outputarr.append(px)
    return outputarr


def main():
    str = input("Enter String To Be Hidden: ")
    location = input("Enter file location: ")

    img, width, height = loadImage(location)

    arr = []
    for c in string:
        arr.append(binary(ord(c)))

    arr = standardiseLength(arr, "0", 8)
    arr = combineBits(arr)
    outputarray = declareArray(height, width, True)

    t = 0
    for y in range(0, height):
        for x in range(0, width):
            r, g, b = img.getpixel((x, y))
            if t < len(arr):
                br = binary(r)
                br = list(br)
                br[-1] = arr[t]
                br = "".join(br)
                r = int(denary(br))
            outputarray[y][x] = (r, g, b)
            t += 1

    outputarray = flattenArr(outputarray)
    output = Image.new("RGB", (width, height))
    output.putdata(outputarray)
    output.save("hidden.jpg")


main()
