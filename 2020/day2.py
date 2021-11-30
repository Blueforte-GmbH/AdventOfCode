with open('datas/input_day02.txt') as file:
    lines = [line.split() for line in file]


def get_counts(instance, password):
    count = 0
    for i in list(password):
        if instance == i:
            count += 1
        elif instance != i:
            pass

    return count

valid_pass_count = 0
for line in lines:
    instance = line[1].strip(':')
    password = line[2]

    # print(f"Instance is {instance} and password is {password}")
    
    count = get_counts(instance=instance, password=password)

    print(f"Count is {count}")

    min_times = int(line[0].split('-')[0])
    max_times = int(line[0].split('-')[1])

    if count >= min_times <= max_times:
        print(f"Password {password} is valid for {line}")
        valid_pass_count += 1

    else:
        print(f"Password {password} invalid {line}")
    
print(f"\n ---- Total valid passwords : {valid_pass_count} ----- ")