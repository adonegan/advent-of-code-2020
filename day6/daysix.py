# PART1

# funtion to return how many unique answers there area
def get_unique_answers(response):
    questions = [] # empty list

    for char in response:
        if char not in questions:
            # will only add character to questions list
            # if it hasn't been seen yet in empty list
            # duplicate handling
            questions.append(char)

    return len(questions) # to know how many unique answers there area

with open('input6.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data ]
# print(data)

sum = 0
currentResponse = '' # empty string
for line in data:
    if line != '':
        # if line is not equal to empty string
        currentResponse += line

    # but if it is a blank line / empty string
    else:
        sum += get_unique_answers(currentResponse)
        # back to blank otherwise we'd be testing the same line again
        currentResponse = ''

# check end of input for blank line
# no blank line :( so it will never hit the check above
# so manually check for last line
sum += get_unique_answers(currentResponse)

print(sum)
