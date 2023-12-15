class Fan:
    def __init__(self):
        self.wings=4
        self.brand="Usha"
    def start(self):
        print("fan is starting")
    def rotate(self):
        print("fan is rotating")
    def stop(self):
        print("fan stopped")
f1=Fan()
f2=Fan()
f1.start()
f1.rotate()
f1.stop()
print("wings=",f1.wings,"brand=",f1.brand)
f2.start()
f2.rotate()
f2.stop()
print("wings=",f2.wings,"brand=",f2.brand)
