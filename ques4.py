def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

num = input("Type your number")
print 'sum of digit is ', sum_digits(num)