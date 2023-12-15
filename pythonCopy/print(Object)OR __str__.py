class Demo:
    def __init__(self):
        self.name="neha"
    def disp(self):
        print("Inside disp()")
    def __str__(self):
        return self.name
d1=Demo()
print(d1)
d2=Demo()
print(d2)
print(object)
