with open('input13.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data ]
    # split commas
    data[1] = data[1].split(',')

def get_id_minutes():
    arrival = int(data[0])
    ids = data[1]

    # search lowest wait time
    lowest = 99999999999999
    lowID = 0
    for item in ids:
        if item != 'x':
            id = int(item)
        else:
            continue
            # don't need to do anything if it's an 'x'
            # we can just ignore it

        idMultiple = arrival // id
        difference = (id * (idMultiple+1)) - arrival
        if difference < lowest:
            lowest = difference
            lowID = id

    return lowID * lowest

print(get_id_minutes())

# PART2

def mod_inverse(a,n):

    # find some x such that (a*x) § n == 1
    # (3 * x) % 4 == 1
    # x = 11
    # 3 * 11 = 33
    # 33 % 4 = 1

    a = a % n
    if n == 1:
        return 1
    for x in range(1,n):
        if (a*x) % n == 1:
            return x

# n buses
# bus k at index i departs at a time t+i
# t+i % k == 0
# Chinese remainder theorem
# t % k == -i
# t % k = k-i
# index = (k - (i%k)) % k 

def get_earliest_time():
    ids = []
    fullProduct = 1
    for i in range(len(data[1])):
        item = data[1][i]
        if item != 'x':
            k = int(item)
            i = i % k
            ids.append(((k-i)%k,k))
            fullProduct *= k

    total = 0
    for i,k in ids:
        partialProduct = fullProduct // k

        inverse = mod_inverse(partialProduct,k)
        assert (inverse * partialProduct) % k == 1

        term = inverse * partialProduct * i 
        total += term

    return total % fullProduct


print(get_earliest_time())

# A lot of number theory
# Codealong with Dylan Codes: https://www.youtube.com/watch?v=3oVWRPzT2JA
# Chinese remainder theorem: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
# Modular inverse: https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
