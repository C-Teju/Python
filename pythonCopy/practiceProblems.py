'''wap to convert all first letters to caps'''
'''a=input("Enter a sentence")
print(a.title())'''

#-----------------------------------------------------------------------------

'''wap that takes a str and char input, create a new str by returning
all occurances of the user entered string'''
'''s=input("enter a string")
ch=input("Enter a character to be deleted from the string")
print(s.replace(ch,''))'''

#-----------------------------------------------------------------------------

'''wap to find the sum of all digits from a user given STRING'''
'''s=input('enter string with numbers in it')
count=0
for i in s:
    if (i.isdigit()):
        count=count+int(i)
print(count)'''

#-----------------------------------------------------------------------------

'''WAP that takes a sentence as an input where each word in the sentence is
seperated by a space. The function should replace each blank with a hyphen
and then print the modifird sentence '''
'''s=input("enter a string")
print(s.replace(' ','-'))'''

#-----------------------------------------------------------------------------


'''WAP to find largest and smallest element present in a list'''
'''lst=list(eval(input("Enter elements of a list")))
print(lst)
print("Minimum=",min(lst))
print("Maximum=",max(lst))'''

#-----------------------------------------------------------------------------

'''WAP to print
******
******
******'''
'''for i in range(3):#0,1,2 will be the three rows because range(Start(0),End(3))
    for j in range (6):#number of columns
        print('*',end=(' '))
    print()

row=int(input("Enter the no of rows"))
column=int(input("Enter the no of column"))

for i in range (row):
    for j in range (column):
        print('*',end=(' '))
    print()'''

#-----------------------------------------------------------------------------


'''increasing * pattern'''
'''n=5
for i in range(n):#when i is 0(i.e the frst line)...
    for j in range(i+1):#..j has to rotate 1 time to print 1 star in first line
        print('*',end=(' '))
    print()'''
        

#-----------------------------------------------------------------------------


'''decreasing pattern'''
n=5
for i in range (n):
    for j in range(n-i):
         print('*',end=(' '))
    print()

#-----------------------------------------------------------------------------

'''WAP to count the number of times a character occurs in the given string'''
'''WAP to replace all vowels in string to *'''
'''WAP which reverses a string and stores the reversed string into a new
string.'''
'''WAP that inputs a line of text and prints out the count of vowels in it'''
'''WAP to input a line of text and print the biggest word(length wise) from it'''

