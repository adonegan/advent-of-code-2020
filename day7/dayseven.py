# how many bags hold our shiny gold bag?
# using recursive functions

with open('input7.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data ] # get rid of newline characters

# PART 1
def get_num_bags(color):
    lines = [ line for line in data if color in line and line.index(color) != 0 ]
    # line.index(color) returns first index in string that the color shows up

    allColors = [] # keep track of the colors we've checked

    if len(lines) == 0:
        return []

    else:
        colors = [ line[:line.index(' bags')] for line in lines ]
        colors = [ color for color in colors if color not in allColors ]
        # only checking colors that have not been checked before

        for color in colors:
            allColors.append(color)
            bags = get_num_bags(color)

            allColors += bags

        uniqueColors = []
        for color in allColors:
            if color not in uniqueColors:
                uniqueColors.append(color)

        return uniqueColors

colors = get_num_bags('shiny gold') # all the rules containing 'shiny gold'
print(len(colors))
# output is 155

# PART2
def get_bag_count(color):
    # need to get the rule for each color each time
    rule = '' # blank line
    for line in data:
        if line[:line.index(' bags')] == color:
            rule = line

    # base case for recursive function
    if 'no' in rule:
        return 1

    rule = rule[rule.index('contain')+8:].split()
    # get everything after the word 'contain' and split
    # split makes four items per color

    total = 0
    i = 0
    while i < len(rule):
        count = int(rule[i])
        color = rule[i+1] + ' ' + rule[i+2]

        total += count * get_bag_count(color)

        i += 4

    return total + 1

count = get_bag_count('shiny gold')
print(count - 1)
# - 1 to remove original shiny gold bag
# output is 54803
 
# codealong with Dylan Codes https://www.youtube.com/watch?v=7IOd7wvxDX0