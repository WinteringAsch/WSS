p = int(input())

for i in range(p):
    line = input()
    H, W, N = line.split()
    H=int(H)
    W=int(W)
    N=int(N)
    if N%H ==0:
    	print(int(N/H) + H*100)
    else:
    	print((int(N/H)+1)+(N%H)*100)
   
