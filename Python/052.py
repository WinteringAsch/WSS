import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Housepark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다." %(self.fullname, where))

pey = Housepark("성우")
print(pey.travel("태국")) #none이 출력되는 이유는, 함수를 print할때 결과값이 출력되기 때문

class Housekim(Housepark):
    lastname = "김"
    def travel(self, where, day):
        print("%s, %s여행을 %d일 가다." %(self.fullname, where, day))
juliet = Housekim("줄리엣")
print(juliet.travel('프랑스', 12))
