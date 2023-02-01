def alpha():
    x1 = 1
    y1 = 0
    x2 = 1
    y2 = 0
    while x1 <= 100:
        pow1 = pow(x1, 2)
        y1 += pow1
        x1 += 1
    print(y1)
    while x2 <= 100:
        y2 += x2
        x2 += 1
    pow2 = pow(y2, 2)
    print(pow2)

    result = pow2 - y1
    print(result)


alpha()
