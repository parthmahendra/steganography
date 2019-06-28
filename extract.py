def binary(i, t=0):
    f = int(str(i)[:1])
    if f == 1:
        t += (2 ** len(i))
    if len(i) != 1:
        binary(int(str(i)[1:]))
    else:
        return t += 
