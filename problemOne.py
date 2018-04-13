def multiples(num):
    start = 0
    sum = 0
    while start < num:
        if start % 3 == 0 or start % 5 == 0:
            sum += start
        start = start + 1
    return sum


print(multiples(10))
print(multiples(1000))

