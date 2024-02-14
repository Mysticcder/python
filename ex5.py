def even(b):
    return b % 4
num = 2
if num == 0:
    print("even")
else:
    print("odd")

num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even number".format(num))