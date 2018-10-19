class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("Yeaaaa")

eagle = Eagle()
eagle.fly()
n = 5


for i in range (1,10):
    print("%d * %d = %d" %(n, i, n*i))
