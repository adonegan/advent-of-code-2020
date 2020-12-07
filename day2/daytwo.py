import csv

# Part 1
with open('input.csv') as data:
    reader = csv.reader(data, delimiter=' ')

    validCount = 0 #valid counts we found
    for row in reader:
        policy, letter, pas = row[0], row[1][0], row[2] 
        # print(policy,letter,pas)
        # row[1][0] = only want 1st element of the second row, not the colon

        i = policy.index('-') # find index of dash character
        lower = int(policy[:i]) # everything from before
        upper = int(policy[i+1:]) # everything after dash
        # print(policy, lower, upper)

        count = 0
        for character in pas:
            if character == letter:
                count += 1

        if count >= lower and count <= upper:
            validCount += 1

print(validCount)
# Part 1 output 458

# Part 2
# with open('input.csv') as data:
#     reader = csv.reader(data, delimiter=' ')

#     validCount = 0 
#     for row in reader:
#         policy, letter, pas = row[0], row[1][0], row[2] 

#         i = policy.index('-') 
#         lower = int(policy[:i])
#         upper = int(policy[i+1:]) 

#         count = 0
#         first = pas[lower-1] == letter # no concept of position zero
#         last = pas[upper-1] == letter

#         if (first and not last) or (last and not first):
#             validCount += 1

# Part 2 output 342

# Codealong https://www.youtube.com/watch?v=nyTAQ-HqAk0