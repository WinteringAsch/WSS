a = 2
b = 3
n = []
for k in range(15):
    n.append(k+1)
for i in range(a):
    for j in range(b-1, -1, -1):
        for m in range(j-1, -1, -1):
            n[j] += n[m]
        print(n[j])
    print('new floor')
print(n[b-1])
