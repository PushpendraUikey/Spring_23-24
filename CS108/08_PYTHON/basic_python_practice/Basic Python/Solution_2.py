import sys

file = sys.argv[1]

desired_num = set()
with open(file) as file:
    numbers=file.readlines()

for number in numbers:
    numbers_string = number.split(',')
    num_as_number = [int(num.strip()) for num in numbers_string]
    for num in num_as_number:
        desired_num.add(num)

print(len(desired_num))