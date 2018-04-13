def evenFibonacci(ceiling):
    first = 1
    second = 2
    sum = 0
    while second < ceiling:
        if first % 2 == 0:
            sum += first
        first = first + second
        if second % 2 == 0:
            sum += second
        second = first + second
    print(sum)

evenFibonacci(4000000)

