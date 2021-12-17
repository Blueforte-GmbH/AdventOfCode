import numpy as np

from helpers.utils import open_lines
lines = open_lines(inputfile='./inputs_test/inputs_day04_test.txt')
lines = [x for x in lines if x != []]

boards = lines[1:]
chosen_numbers = lines[0][0].strip(',').split(',')[0:5]


increment = 5
end_l = len(boards)

for i in np.arange(0, end_l, increment):
    if i == 0:
        b = boards[i: increment]
    else:    
        b = boards[i: (i+increment)]

