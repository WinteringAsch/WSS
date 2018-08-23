'''
a = input("Insert contents here : ")
print(a)
'''

for i in range (10):
    print(i, end= ' ') #end 말고 다른건 없나?
print('\n')
f = open("newfile.txt", 'w')
for i in range (10):
    data= "#%d line.\n" %i
    f.write(data)
f.close()

f = open("newfile.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("newfile.txt", 'a')
for i in range (11, 20):
    data= "#%d line.\n" %i
    f.write(data)
f.close()

f = open("newfile.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
