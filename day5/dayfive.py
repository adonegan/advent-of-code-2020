# PART1

# write a function to get row
# write a function to get column

def get_row(seat):
    # define lower and upper
    lower = 0
    upper = 127

    for i in range(6):
        # go through first 7 characters of seats
        half = (upper + lower)//2 
        # average divided by 2
        if seat[i] == 'F':
            # upper now not 127 but half that
            upper = half

        elif seat[i] == 'B':
            # 64-127
            lower = half + 1 

    if seat[6] == 'F':
        return lower

    else:
        return upper

def get_col(seat):
    upper = 7
    lower = 0

    for i in range(2):
        half = (upper + lower)//2
        if seat[i] == 'L':
            upper = half
        
        elif seat[i] == 'R':
            lower = half + 1 

    if seat[2] == 'L':
        return lower

    else: 
        return upper

largest = 0
# First step: open and read input file
with open('input5.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data ] 
    # print(data)

    for seat in data:
        row = get_row(seat[:7]) # the Fs and Bs
        col = get_col(seat[7:]) # the Rs and Ls

        id = row * 8 + col
        if id > largest:
            largest = id

print(largest)