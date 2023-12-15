#for loop
for i in "kodnest":
    print(i, end='-')
'''Wap to print all the vowels in a string'''
s1=input("Enter a  string")
for i in s1:
    if i in 'aeiouAEIOU':
        print (i,end=' ')
print("these are vowels")    
'''Wap to print all the consonents in a string'''

for i in s1:
    if i not in 'aeiouAEIOU':
        print (i,end=' ')      
print("these are consonents")


'''WAP to print numbers from 1-10 using for loop'''
for i in range(1,11,1):
    print(i,end=' ')
for i in range(0,9,-1):
    print (i)
