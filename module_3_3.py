# 1
def print_params (a = 1, b = 'string', c = True):
    print(a, b, c)

print_params()

def print_params (*args):
    print(args)

print_params(1, 2, 3, 4, 5)
print_params()

# 2
def print_params (a, b, c):
    print(a, b, c)

values_list = [123, False, 'string']
values_dict = {'a': 456, 'b': True, 'c': 'STRING'}
print_params(*values_list)
print_params(**values_dict)

# 3
values_list_2 = [3.14, 'StRiNg' ]
print_params(*values_list_2, 42)
