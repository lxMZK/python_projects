def arb_args(*args):
    for i in args:
        print(i)


def inner_func(a, b):
    def func_a(a, b):
        return a + b

    def func_b(a, b):
        return a * b
    print(func_a(a, b)+func_b(a, b))


def lunch_lady(name, pref='Mystery Meat'):
    print(name, pref)


def sum_n_product(a, b):
    return a+b, a*b


alias_arb_args = arb_args


def arb_mean(*int):
    sum = 0
    for i in int:
        sum += i
    return sum/len(int)


def arb_longest_string(*str):
    max = 0
    long = ''
    for i in str:
        if len(i) > max:
            max = len(i)
            long = i
    return long


def name_args(*items):
    key = 1
    for i in items:
        print(f"{key}:{i}")
        key += 1


def all_true(iter):
    return all(iter)


def one_true(iter):
    return any(iter)


def recursive_factorial(n):
    if n <= 1:
        return 1
    else:
        return n*recursive_factorial(n-1)


def recursive_deduplicate(input, i=0):
    if len(input) <= 1 or i == len(input)-1:
        return input
    else:
        if input[i] == input[i+1]:
            return recursive_deduplicate(input[0:i]+input[i+1:], i)
        else:
            return recursive_deduplicate(input, i+1)


def recursive_reverse(str, i=0):
    if len(str) == 0:
        return ""
    elif i == len(str)-1:
        return str[0]
    else:
        return str[-1-i] + recursive_reverse(str, i+1)


def max_num(a, b, c):
    return max([a, b, c])


def mult_list(input):
    if len(input) == 0:
        return 0

    total = 1
    for i in input:
        total *= i

    return total


def rev_string(str):
    print(str[::-1])


def num_within(n, min, max):
    return n in range(min, max+1)


def pascal(n):
    triangle = [[1], [1, 1]]
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev)+1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1]
                               [i-1]+triangle[row_number-1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        for row in triangle:
            print(row)


print(max_num(13290, 3, 100))
print(mult_list([1, 3, 4, 2, 1, 2]))
rev_string('hello')
print(num_within(49, 1, 49))
print(num_within(49, 1, 32))
pascal(10)
pascal(5)
