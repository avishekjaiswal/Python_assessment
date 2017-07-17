def is_Power_of_two(n):
        return n > 0 and (n & (n - 1)) == 0

n =input("Enter your nunmber")
print(is_Power_of_two(n))