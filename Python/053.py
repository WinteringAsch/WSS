try:
    4/0
except ZeroDivisionError as e:
    print(e)

try:
    f = open('foo.txt', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    f.close()
try:
    f = open("wtf.txt", 'r')
except FileNotFoundError:
    pass
    
