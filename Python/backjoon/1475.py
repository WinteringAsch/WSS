s = 6666
s = str(s)
req = []
for i in range(10):
    req.append(0)
for i in range(len(s)):
    n = int(s[i])
    req[n] += 1
req[9] += req[6]
if req[9] % 2 == 1:
    req[9] = int(req[9]/2)+1
else:
    req[9] = int(req[9]/2)
req[6] = 0
print(max(req))
