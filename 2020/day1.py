
# open file to read as ints 
with open('datas/input_day01.txt') as file:
    lines = [int(line) for line in file]


test = [1721, 979,366 ,299 ,675 ,1456]

# Part 1
# test with a simple list comprehension
# get the sum of two entries which sum to 2020
condtion_1 = [(i*j) if i+j == 2020 else 0 for i in lines for j in lines]
puzzle_1 = max(condtion_1)
print(puzzle_1)


# Part 2
condtion_2 = [(i*j*k) if i+j+k == 2020 else 0 for i in lines for j in lines for k in lines]
print(max(condtion_2))



# TODO: Write tests
