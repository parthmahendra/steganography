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
