# 1.
for x in range(0, 151):
    print(x)

# 2.
for x in range(5, 1005, 5):
    print(x)

# 3.
for x in range(1, 101):
    if x % 10 == 0:
        print('coding')
    elif x % 5 == 0:
        print('coding dojo')
    else:
        print(x)

# 4.
sum = 0
for x in range(0, 500001):
    if x %  2 !=0:
        sum += x
print(sum)

# 5.
for x in range(2018, 0, -4):
    if x > 0:
        print(x)

# 6.
for x in range(6, 18, 3):
    if x % 3 == 0:
        print(x)