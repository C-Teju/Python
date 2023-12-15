def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

ref=fibonacci()
n=int(input('enter a no'))
for i in range(n):
    print(next(ref))
    

    
