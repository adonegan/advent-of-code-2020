
with open('input8.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data ]

# PART1
def get_acc():
    acc = 0
    line = 0
    instructions = []

    # not using for loop because increase isn't always by 1
    while line not in instructions:
        instructions.append(line)

        currentInstruction = data[line]     
        # first line acc +14
        currentInstruction = currentInstruction.split() # becomes ['acc', '+14']
        cmd = currentInstruction[0] # gets acc / all item in this index position in cmd variable
        num = currentInstruction[1] # gets +14
        if '+' in num:
            num = int(num[1:])
        else:
            num = int(currentInstruction[1])

        if cmd == 'acc':
            acc += num
            line += 1

        elif cmd == 'jmp':
            line += num

        elif cmd == 'nop':
            line += 1

    return acc

acc = get_acc()
print(acc)
# output 1675

# PART2
def get_acc_eof():
    # no input as data is a global variable
    acc = 0
    line = 0
    instructions = []

    while line not in instructions:
        instructions.append(line)

        currentInstruction = data[line]     
        currentInstruction = currentInstruction.split()
        cmd = currentInstruction[0]
        num = currentInstruction[1] 
        if '+' in num:
            num = int(num[1:])
        else:
            num = int(currentInstruction[1])

        if cmd == 'acc':
            acc += num
            line += 1

        elif cmd == 'jmp':
            line += num

        elif cmd == 'nop':
            line += 1

        if line >= len(data):
            return acc, True # return as tuple

    return acc, False


for i in range(len(data)):
    if 'jmp' in data[i]:

        data[i] = data[i].replace('jmp', 'nop')
        acc, found = get_acc_eof()

        if found:
            print(acc)
            break
        else:
            data[i] = data[i].replace('nop', 'jmp')

# output 1532
# Codealong with Dylan Codes https://www.youtube.com/watch?v=0G5uWSphSDc