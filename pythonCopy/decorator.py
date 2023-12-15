def hi(func):
    def histring(a):
        if a=='hi':
            print("error")
        else:
            func(a)
    return histring
@hi
def string(a):
    print('Welcome',a)

string('hi')
