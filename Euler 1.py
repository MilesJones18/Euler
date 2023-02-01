L = []
total = 0
for x in range(1, 1000):
    if x % 3 == 0 or x % 5 == 0:
        L.append(x)
    else:
        pass

print(sum(L))
