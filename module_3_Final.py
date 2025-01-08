data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


def unpack_data_structure(data):
    """
    Приводит исходный массив данных к удобному для вычисления формату
    Распаковывает элементы вложенных структур данных в один список
    """
    unpacked_list = []
    stack = [data]
    while stack:
        item = stack.pop()
        if isinstance(item, list) or isinstance(item, tuple):
           stack.extend(item[::-1])
        elif isinstance(item, dict):
            stack.extend(item.keys())
            stack.extend(item.values())
        elif isinstance(item, set):
            stack.extend(list(item))
        else:
            unpacked_list.append(item)
    return unpacked_list

unpacked_data = unpack_data_structure(data_structure)


def sum_num (*args):
    """
    Подсчёт суммы всех чисел и длин всех строк
    """
    total_sum = 0
    for item in args[0]:
        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, str):
            total_sum += len(item)
    return total_sum


final_sum = sum_num(unpacked_data)
print(final_sum)