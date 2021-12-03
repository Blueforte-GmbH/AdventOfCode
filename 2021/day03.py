from helpers.utils import open_inputs
lines = open_inputs(inputfile='./2021/inputs/input_day03.txt')



get_byte = lambda x:list(x[0])

lines = [['00100'],
        ['11110'],
        ['10110'],
        ['10111'],
        ['10101'],
        ['01111'],
        ['00111'],
        ['11100'],
        ['10000'],
        ['11001'],
        ['00010'],
        ['01010']]

# for bit in range(1,13):


def get_most_common(n_bit):

    count_0 = 0
    count_1 = 0

    for i in range(0, len(lines)):

        bytes = list(map(int, get_byte(lines[i])))

        # print(bytes)

        if bytes[n_bit] == 0:
            count_0 += 1
        elif bytes[n_bit] == 1:
            count_1 += 1

        var = {count_0 : "count_0", count_1 : "count_1"}
        most_common = var.get(max(var))

    print(f"Most common : {most_common}")

    return most_common

[get_most_common(i) for i in range(5)]

# for bit in range(1,13):

#     for line in lines:
