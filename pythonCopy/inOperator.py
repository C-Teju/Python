'''#1)WAP to check if the number is present between 1-10 excluding 1 and 10'''
'''num=int(input("Enter a number"))
if num>1 and num<10:
    print(num,"is in between 1-10")
else:
    print(num,"is not in between 1-10")'''
'''2'''
'''3'''
'''4)Wap a calculator program :1-add, 2-sub, 3-mul, 4-div or invalid choice'''
n1=int(input("Enter a number"))
n2=int(input("Enter 2nd number"))
ch=int(input("1-add, 2-sub, 3-mul, 4-div "))
if ch==1:
    print(n1+n2)
elif ch==2:
    print(n1-n2)
elif ch==3:
    print(n1*n2)
elif ch==4:
    print(n1/n2)
else:
    print("Invalid choice")
