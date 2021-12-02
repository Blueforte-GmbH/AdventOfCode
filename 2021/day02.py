from helpers.utils import open_inputs
lines = open_inputs(inputfile='./2021/inputs/input_day02.txt')

# Part 1
hp = 0
depth = 0

for line in lines:
    if line[0] == 'forward':
        hp = hp + int(line[1])
    elif line[0] == 'down':
        depth = depth + int(line[1])
    elif line[0] == 'up':
        depth = depth - int(line[1])

final_position = hp * depth
print(f"Final position part 1: {final_position}")


# Part 2
hp = 0
depth = 0
aim = 0

for line in lines:
    if line[0] == 'forward':
        hp = hp + int(line[1])
        depth = depth + (aim * int(line[1]))
    elif line[0] == 'down':
        aim = aim + int(line[1])
    elif line[0] == 'up':
        aim = aim - int(line[1])      
        
final_position_2 = hp * depth
print(f"Final position part 2: {final_position_2}")
