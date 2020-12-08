# PART1

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
# all fields that must be valid, not 'cid' is excluded

def is_valid_passport(pp):
    """
    check if password is valid by 
    cross checking with fields in 
    list above
    """
    for field in fields:
        if field not in pp:
            return False
    return True


with open('input4.txt') as file:
    passport_data = file.readlines()
    passport_data = [line.strip() for line in passport_data]
    # print(passport_data)

validCount = 0

currentPassport = '' 
# must be defined
# to avoid: NameError: name 'currentPassport' is not defined

for line in passport_data:
    if line != '':
        currentPassport += ' ' + line
    else:
        if is_valid_passport(currentPassport):
            validCount += 1
        
        currentPassport = ''

if is_valid_passport(currentPassport):
    validCount += 1

print(validCount)
# output 245

# Codealong with Dylan Codes https://www.youtube.com/watch?v=kQESIOLQb-Y