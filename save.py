def declareArray(m, n, integer):
    arr = []
    char = 0 if integer else ""
    for y in range(m):
        arr.append([])
        for x in range(n):
            arr[y].append(char)
    return arr

def binary(i):
    n = 0
    binarr = []
    while 2 ** n <= i:
        n += 1
    for x in range(n-1,-1,-1):
        if (2 ** x) <= i:
            i -= (2 ** x)
            binarr.append("1")
        else:
            binarr.append("0")
    return "".join(binarr)
