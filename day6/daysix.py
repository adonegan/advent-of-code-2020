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

    return len(questions) # to know how many unique answers there are

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
# output 6532

# PART 2

def get_unique_answer_all(responses):
    questions = []

    for char in responses[0]:
        # checking first line
        # needs to be reset for all characters
        inAllLines = True 
        for line in responses:
            if char not in line:
                inAllLines = False

        if inAllLines and char not in questions:
            questions.append(char)

    return len(questions)

sum = 0
currentResponse = []
# Keep lines separate in a list
for line in data:
    if line != '':
        currentResponse.append(line)
    else:
        sum += get_unique_answer_all(currentResponse)
        currentResponse = []

sum += get_unique_answer_all(currentResponse)

print(sum)
# output 3427

# Codealong with Dylan Codes https://www.youtube.com/watch?v=_pPgnryUEDw