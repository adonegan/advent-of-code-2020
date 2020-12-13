
with open('input9.txt') as file:
    data = file.readlines()
    data = [ int(line.strip()) for line in data ] # int as list is all numbers

# PART1
def get_bad_number():
    # first 25 numbers are preamble
    # 26th number is the one we want 
    # see if sum can be found for it
    # loop from 26th to the end
    # we don't want to check the first 25 numbers
    for i in range(25, len(data)):
        # range(start,stop)
        preamble = data[i-25:i] # 0-24
        num = data[i]
        found = False

        for j in range(len(preamble)-1):
            for k in range(j+1,len(preamble)):
                if preamble[j] + preamble[k] == num:
                    found = True
                    break
            if found == True:
                break
        
        if found == True:
            continue

        return num
    
num = get_bad_number()
print(num)
# output 18272118


# PART2
def get_key():
    bad_num = get_bad_number()
    found = False

    for i in range(len(data)-1):
        nums = [data[i]]
        for j in range(i+1,len(data)):
            nums.append(data[j])

            if sum(nums) == bad_num:
                found = True
                break

            elif sum(nums) > bad_num:
                break
        
        if found == True:
            break

    return min(nums) + max(nums)

print(get_key())
# output 2186361

# Codealong with Dylan Codes https://www.youtube.com/watch?v=kIuTRDuCBmU
