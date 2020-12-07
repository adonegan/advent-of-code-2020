
with open('input3.txt') as file: 
    map = file.readlines() 
    map = [line.strip() for line in map] 
    # strip / remove newline characters '\n'
    # print(map)

# PART1

treeCount = 0 # start treeCount at zero (we haven't hit any trees yet lol)
row,col = 0,0 # starting position is "open square (.) in top left corner"

while row+1 < len(map): 
    # +1 to help stop before we go out of bounds 
    # to prevent this error: IndexError: list index out of range
    row += 1
    col += 3
    

    # the space to check 
    # map (row and col) that we're in
    # modulo it (return remainder) by the size of the map - why??
    # "eventually the col will be out of bounds"
    # to prevent this error: IndexError: string index out of range
    # if space is equal to tree, count the tree
    space = map[row][col % len(map[row])] 
    if space == '#': 
        treeCount += 1

print(treeCount)
# part1 output 159


# PART2

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)] # list of tuples for unchanging values
total = 1
# for multiplying instead of adding 
# if it was zero, total would be zero

for slope in slopes:
    # wrap in for loop to iterate over each tuple
    treeCount = 0
    row,col = 0,0

    while row+1 < len(map): 
        row += slope[1] # access second value in tuples
        col += slope[0] # access first value in tuples

        space = map[row][col % len(map[row])] 
        if space == '#': 
            treeCount += 1

    total *= treeCount

print(total)
# part2 output 6419669520
 
# Codealong with Dylan Codes https://www.youtube.com/watch?v=rWXUsiK3Hl4