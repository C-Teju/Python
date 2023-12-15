#methods
#type 1:- no input no output
def add():
    a=10
    b=20
    print(a+b)
add()

#type 2:- no input but there is output
def add():
    a=10
    b=20
    return a+b
print(add())

#type 3:- there is input and output
def add(a,b):
    return a+b
print(add(10,20))

#type 4:-there is input no output
def add(a,b):
    print(a+b)
add(10,20)
