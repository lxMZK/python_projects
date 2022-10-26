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


name_args('a', 'b', 'c', 'd', 'e')
print(all_true([True, True, True]))
print(all_true((True, False)))
print(one_true([True, True, True]))
print(one_true((False, False)))
print(recursive_factorial(5))
print(recursive_factorial(8))
print(recursive_deduplicate("AABBCCDD"))
print(recursive_reverse("apple"))
