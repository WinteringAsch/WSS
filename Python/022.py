a = [0,1, [2,3]]

print(a[1])
print(a[2][1])

b = [4, 5, 6]

c = a+b
d = a*2
print(c)
print(d)
e = [1,2,3]
f = [1,2,3]
e[1:2] = ['a', 'b', 'c'] # e의 1~2 사이를 바꿈
f[1] = ['a', 'b', 'c'] # f의 1번째 요소를 바꿈
print(e)
print(f)
e[1:3] = []
print(e)
