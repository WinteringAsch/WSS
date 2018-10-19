line = 'YeahIlikeMusicandTekken7'
print(len(line))

n = len(line)
r = int(n/10)
l = n%10
p = 0
for i in range(0,r+1):
    if i == r:
        for j in range(0, l):
            print(line[p], end = '')
            p += 1
    else:
        for j in range(0, 10):
            print(line[p], end = '')
            p += 1
    print()
