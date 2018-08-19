a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80]
num = 0

for mark in marks:
    num = num + 1
    if mark >= 60:
        print("#%d student have passed" % num)
    else:
        print("#%d student have not passed" % num)

b = [1, 2, 3, 4]
result = [num*3 for num in b]
print(result)
result2 = []
for num in b:
    result2.append(num*4)
print(result2)
