head="Hello"
tail='World!'

print((head +' '+ tail+'\n') * 5)
print(tail[-2])
print(head[2:3]) # 구간 조심하기

test = 'Pithon'
test2 = test[0] + 'y' + test[2:6]

print(test2)

print("Success rate of Ferghus is %d%%" %90) # %d와 함께 %표시를 위해선 %%

print("%10s" %test2) #정렬하기
