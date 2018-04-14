def is_prime(num):
    for i in range(2, num / 2 + 1):
        if num % i == 0:
            return False
    return True


def largest_prime_factor(num):
    result = 0
    for i in range(2, num / 2):
        print(i)
        if is_prime(i) and num % i == 0:
            print(i)
            result = i
    return result


print(is_prime(2))

print(largest_prime_factor(600851475143))
