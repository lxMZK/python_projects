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


arb_args('hello', 'world')
inner_func(1, 2)
lunch_lady('alex')
lunch_lady('bob', 'chicken')
print('(sum, product): ', sum_n_product(1, 2))
alias_arb_args('hello', 'world', '2')
print(arb_mean(1, 2, 3, 4))
print(arb_longest_string('a','bb','ccc','dddd','e'))