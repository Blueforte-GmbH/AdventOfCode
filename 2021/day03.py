from helpers.utils import open_inputs
lines = open_inputs(inputfile='./2021/inputs/input_day03.txt')

get_byte = lambda x:list(x[0])

# lines = [['00100'],
#         ['11110'],
#         ['10110'],
#         ['10111'],
#         ['10101'],
#         ['01111'],
#         ['00111'],
#         ['11100'],
#         ['10000'],
#         ['11001'],
#         ['00010'],
#         ['01010']]

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
        least_common = var.get(min(var))

    print(f"Most common : {most_common}")
    if most_common == 'count_0':
        most_bit = 0
    else:
        most_bit = 1

    if least_common == 'count_0':
        least_bit = 0
    else:
        least_bit = 1

    return most_bit, least_bit


gamma_rate = []
for i in range(12):
    most_bit, _ = get_most_common(i)
    gamma_rate.append(most_bit)
gamma_rate  = int(''.join(map(str, gamma_rate)), 2)


epsilon_rate = []
for i in range(12):
    _, least_bit = get_most_common(i)
    epsilon_rate.append(least_bit)
epsilon_rate  = int(''.join(map(str, epsilon_rate)), 2)



print(f"Power Consumtion : {gamma_rate * epsilon_rate}")