'''wap to print numbers from 1-10 and stop printing if number is equal to 7'''
#a)
for i in range(1,11):
    if i==7:
        break
    print(i,end=' ')
print()    
print("loop terminated (break)")
#b)
for i in range(1,11):
    if i==7:
        continue
    print(i,end=' ')
print()    
print("loop terminated (continue)")
