
#3n(n-1)+1
x = 9
k = 1
while x > (k*(k+1)/2):
    k += 1
k -= 1
x = x - (k*(k+1)/2)
if k % 2 == 0:
    a = str(int(k-x+2))
    b = str(int(x))
else:
    a=str(int(int(x)))
    b=str(int(int(k-x+2)))
print(a+'/'+b)
