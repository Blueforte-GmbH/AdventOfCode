from helpers.utils import open_inputs

lines = open_inputs(inputfile='./2021/inputs/input_day01.txt')

increments = 0
for i in range(len(lines)):
    if i == len(lines) - 1:
        break
    else:
        j = i + 1
        if int(lines[j][0]) > int(lines[i][0]):
            increments += 1

print(f"Total increments part 1: {increments}")


# Part 2
increments = 0
for i in range(len(lines)):
    if i == len(lines) - 3:
        break
    else:
        j = i + 1 
        if sum(list(map(int, sum(lines[j:j+3], [])))) > sum(list(map(int, sum(lines[i:i+3], [])))):
            increments += 1
print(f"Total increments part 2: {increments}")