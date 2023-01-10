# Simple Lambda Functions -----------------
x = 5
y = 6

func_square = lambda x: x ** 2
sqr = func_square(5)
print(f'Square of {x}: {sqr}')

func_cube = lambda x: x ** 3
cube = func_cube(5)
print(f'Cube of {x}: {cube}')

func_sum = lambda x, y: x + y
sum = func_sum(x, y)
print(f'Sum of {x} and {y}: {sum}')

func_product = lambda x, y: x * y
product = func_product(x, y)
print(f'Product of {x} and {y}: {product}')

list_of_tuples = [('john', 5), ('jane', 8), ('jack', 2), ('joe', 12), ('jason', 1)]

sort_number = sorted(list_of_tuples, key=lambda x: x[1])
print(list(sort_number))

sort_name = sorted(list_of_tuples)
print(list(sort_name))

sort_name_len = sorted(list_of_tuples, key=lambda x: len(x[0]))
print(list(sort_name_len))

sort_name_len_reverse = sorted(list_of_tuples, key=lambda x: len(x[0]), reverse=True)
print(list(sort_name_len_reverse))

numbers_list = [6, 18, 21, 45 , 2]

numbers_sqared = map(lambda x: x ** 2, numbers_list)
print(list(numbers_sqared))

numbers_cubed = map(lambda x: x ** 3, numbers_list)
print(list(numbers_cubed))

numbers_evnsqr_oddcub = map(lambda x: x ** 2 if x % 2 == 0 else x ** 3, numbers_list)
print(list(numbers_evnsqr_oddcub))

strings_list = ['guitar', 'clarinet', 'trumpet', 'piano', 'violin', 'drums', 'flute', 'cello', 'recorder', 'ukulele']

strings_len_lt5 = filter(lambda x: True if len(x) > 5 else False, strings_list)
print(list(strings_len_lt5))

strings_len_lt5_stvow = filter(lambda x: True if (len(x) > 5) and (x[0].lower() in ['a', 'e', 'i', 'o', 'u']) else False, strings_list)
print(list(strings_len_lt5_stvow))









