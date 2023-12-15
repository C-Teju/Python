#for loop II
#WAP tp print the numbers from 1-10 on one line using for loop
for i in range(1,11):
    print(i,end='')

#wap to create a list, tuple having numbers in range 20-30  
print(list(range(20,31)))
print(tuple(range(20,31)))


#eval()
a1='5'
b1=eval(a1)
print(b1,type(b1))

a2='55.6'
b2=eval(a2)
print(b2,type(b2))

a3='66+4j+5j'
b3=eval(a3)
print(b3,type(b3))

'''wap to print all the even numbers from a list.
#note: take all list elements from the user.'''


'''lst=list(eval(input("enter elements comma seperated")))'''


#wap to create aduplicate list of lst=[20,40,50,80] using list comprihension
lst1=[20,40,50,80]
lst2=[i for i in lst1]
print(lst1,lst2)


#wap to filter all the names starting with 'a'
l1=['ankith', 'nikitha', 'punith','deep','akash']
l2=[i for i in l1 if i[0]=='a']
print (l2)
