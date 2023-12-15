#if
age=int(input("Enter your age"))
if age>18:
    print("Inside if")
print("Outside if")    


#if-else
if age>18:
    print("Eligible")
else:
    print("Not Eligible")


#if-elif-else
ch=input("Enter a character").lower()
if ch=='a' or ch=='A':
    print(ch," is a vowel")
elif ch=='e' or ch=='E':
    print(ch," is a vowel")
elif ch=='i' or ch=='I':
    print(ch," is a vowel")
elif ch=='o' or ch=='O':
    print(ch," is a vowel")
elif ch=='u' or ch=='U':
    print(ch," is a vowel")
else:
    print(ch," is a consonent")


#in operator
#1
if ch in'aeiou':
    print(ch, " is a vowel")
else:
    print(ch," is a consonent")

#2
b="Raja Ram Mohan Roy"
if "Ram" in b:
    print("present")

    
#3    
l1=[10,20,30,40,50]
print(30 in l1)
print(30 not in l1)
