import sys

arguments = []
for line in sys.stdin:
    line = line.strip()
    arguments.append(line)

string = arguments[0]
index_s = arguments[1]

index_s = index_s.split(' ')

index_s = [int(num) for num in index_s]

if not all(num in range(len(string)) for num in index_s):
    print("INVALID INPUT")
    exit()

required_string =[]
for num in range(len(string)):
    required_string.append(string[index_s[num]])

strg = ''.join(required_string)

print(strg)
