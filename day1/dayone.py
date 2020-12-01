inputFigs = open('input.txt', 'r')
editedInputFigs = [ int(line) for line in inputFigs.readlines() ] # .readlines() returns a list https://realpython.com/read-write-files-python/

def sumAndMultiply(inputFigs):
    for num in inputFigs:
        magicNum = 2020 - num
        if magicNum in inputFigs:
            return num * magicNum

print(sumAndMultiply(editedInputFigs))

# part two

def threeSumAndMultiply(inputFigs):
    for numOne in inputFigs:
        for numTwo in inputFigs:
            for numThree in inputFigs:
                if numOne + numTwo + numThree == 2020:
                    return numOne * numTwo * numThree

print(threeSumAndMultiply(editedInputFigs))

# credit GLo