def count_down(n):
    if n > 0:
        print(n)
        count_down(n-1)


def natural_numbers(x, i=1):
    if x >= i:
        print(i)
        natural_numbers(x, i+1)


def fibonacci(n):
    if n<1:
        print("incorrect input")
    elif n==1:
        return 0
    elif n==2 or n==3:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def power(a,b):
    print(pow(a,b))

def palindrome(str):
    print(str==str[::-1])

count_down(5)
natural_numbers(9)
print(fibonacci(8))
power(2,4)
palindrome('radar')
