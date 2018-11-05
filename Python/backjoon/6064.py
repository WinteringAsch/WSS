def gcd(a, b):
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return abs(a)
def lcm(a, b):
  gcd_value = gcd(a, b)
  if (gcd_value == 0): return 0
  return int(abs( (a * b) / gcd_value ))

a = 20000
b = 3
x = 20000
y = 1
n = x
if x%b ==0:
    y1 = b
else:
    y1 = x%b
while n < lcm(a,b):
    if (x+a)%b ==0:
        y1 = b
    else:
        y1 = (y1+a)%b
    n += a
    if y1 == y:
        break
if n>lcm(a,b) or x>a or y>b:
    n = -1
print(n)
print(lcm(a,b))
