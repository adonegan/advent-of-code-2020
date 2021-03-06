# PART1 and PART2 

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # all fields that must be valid, note 'cid' is excluded
good_passports = [] # empty list 

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

validCount = 0

currentPassport = '' 
# must be defined
# to avoid: NameError: name 'currentPassport' is not defined

for line in passport_data:
    if line != '':
        currentPassport += ' ' + line
    else:
        if is_valid_passport(currentPassport):
            good_passports.append(currentPassport) # if currentPassport is good, add it to the good_passports list
            validCount += 1
        
        currentPassport = ''

if is_valid_passport(currentPassport):
    good_passports.append(currentPassport)
    validCount += 1

print(validCount)
# print(good_passports)
# output 245


# PART2
# Will need a separate function for each field

def is_valid_byr(byr):
    byr = int(byr)

    if byr < 1920 or byr > 2002:
        return False

    return True


def is_valid_iyr(iyr):
    iyr = int(iyr)

    if iyr < 2010 or iyr > 2020:
        return False

    return True


def is_valid_eyr(eyr):
    eyr = int(eyr)

    if eyr < 2020 or eyr > 2030:
        return False

    return True


def is_valid_hgt(hgt):
    units = hgt[-2:] # second to last character

    if units not in ['in', 'cm']:
        return False

    hgt = int(hgt[:-2])

    if units == 'in':
        if hgt < 59 or hgt > 76:
            return False
    
    elif units == 'cm':
        if hgt < 150 or hgt > 193:
            return False
    
    return True


def is_valid_hcl(hcl):
    if hcl[0] != '#': return False

    if len(hcl[1:]) != 6:
        return False

    return True


def is_valid_ecl(ecl):
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] # don't miss a color!

    if ecl not in colors: 
        return False

    return True


def is_valid_pid(pid):
    if len(pid) != 9:
        return False

    return True


def has_valid_data(passport):
    passport = passport.split() # split long string into list of substrings
    data = {} # to separate data from category

    for item in passport:
        key = item[:3] # first three items
        value = item[4:] # items after the col
        data[key] = value # this will give us our dictionary

    if not is_valid_byr(data['byr']):
        return False

    if not is_valid_iyr(data['iyr']):
        return False

    if not is_valid_eyr(data['eyr']):
        return False

    if not is_valid_hgt(data['hgt']):
        return False

    if not is_valid_hcl(data['hcl']):
        return False

    if not is_valid_ecl(data['ecl']):
        return False

    if not is_valid_pid(data['pid']):
        return False

    return True

validCount = 0
for pp in good_passports:
    if has_valid_data(pp):
        validCount += 1

print(validCount)
# output 133


# Codealong with Dylan Codes https://www.youtube.com/watch?v=kQESIOLQb-Y