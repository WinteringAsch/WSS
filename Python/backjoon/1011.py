
for c in range(1, 20):
    n = 1
    cmp = 0
    while cmp < c:
        if n%2 == 1:
            cmp += int(n/2) + 1
        else:
            cmp += n/2
        #print('cmp = %d'%(cmp))
        n += 1
    print('c = %d, n = %d' %(c, n-1))
