
with open('input10.txt') as file:
    data = file.readlines()
    data = [ int(line.strip()) for line in data ]
    data.sort()

#PART1
data = [0] + data # count first difference
data.append(max(data)+3)
# print(data)

def get_difference_count():
    count1 = 0
    count3 = 0

    for i in range(len(data)-1):
        dif = data[i+1] - data[i]

        if dif == 1:
            count1 += 1 # count1 = count1 + 1

        elif dif == 3:
            count3 += 1

    return count1 * count3

print(get_difference_count())

#PART2
checked = {}
def get_number_ways(position):
    # recursive function
    if position == len(data)-1:
        return 1

    if position in checked:
        return checked[position]

    total = 0
    for i in range(position+1, len(data)):
        if data[i] - data[position] <= 3:
            total += get_number_ways(i)

    checked[position] = total
    return total

print(get_number_ways(0))

# Codealong with Dylan Codes https://www.youtube.com/watch?v=-PMVdWLLkv4
