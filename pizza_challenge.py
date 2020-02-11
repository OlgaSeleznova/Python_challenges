"""
The task is to order as many pizzas as possible.
The pizzeria has different types of pizza, which should be ordered at most one of each type.
Each type of pizza has a specified size: the size is the number of slices in a pizza of this
type. The goal is to order as many pizza slices as possible, but not more than the maximum number.
"""


def read_line(file):
    # read file, split by space and remove newline
    return file.readline().strip('\n').split(' ')


def read_file(file):
    # read file by line, convert values into integers and list of integers
    line1, line2 = read_line(file), read_line(file)
    max_num_slices, pizza_types = int(line1[0]), int(line1[1])
    pizza_pieces = list(map(lambda x: int(x), line2))
    return pizza_pieces, max_num_slices, pizza_types


def append_to_collections(types, values, types_collector, values_collector):
    # append values to collectors of types and values
    types_collector.append(types)
    values_collector.append(values)
    return types_collector, values_collector


def find_sum():
    # iterate through the list of pizza slices, starting from the maximum numbers in reversed order, until it fits the
    # maximum number of slices (target) until there are maximum number of slices possible
    num_pieces, target, pz_types = read_file(my_file)
    remain = target
    types_collector = []
    values_collector = []
    for num in sorted(num_pieces, reverse=True):
        if remain <= target:
            if remain >= num:
                remain = remain - num
                append_to_collections(num_pieces.index(num), num, types_collector, values_collector)
                continue

        else:
            print('something went wrong')
    ordered_pieces = len(set(types_collector))
    ordered_types = sorted(types_collector)
    print('Percentage of ordered pieces from # needed:', (100 * sum(values_collector)) / target)
    print('Ordered types of pizzas is {}.'.format(ordered_types))
    print('Number of ordered pieces is {}.'.format(ordered_pieces))
    return ordered_types, ordered_pieces


my_files = ['a_example.in', 'b_small.in', 'c_medium.in', 'd_quite_big.in', 'e_also_big.in']
for f in my_files:
    my_file = open(f, 'r')
    print(find_sum())
