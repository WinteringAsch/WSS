class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(1, 2)
print(a.sum())
