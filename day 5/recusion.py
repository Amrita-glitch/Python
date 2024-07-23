def num(i=0):
    print(i)
    if i == 5:
        return
    num(i + 1)


result = num()

print(result)
