class Degree:
    def __init__(self,temp):
        self.temp=temp

    def convert(self):
        return self.temp*1000


a=Degree(float(input("Enter a number : ")))
print(a.__dict__['temp'])