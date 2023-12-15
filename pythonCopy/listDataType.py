#Operations on lists
l1=[10,20,40,30,50,20]
print(l1)
'''#it stores both homogeneous and hetrogeneous data 
#It is ordered collectoin of data(data displayed in the same order of input)'''
#append()
print("after append()")
l1.append(90)
print(l1)
'''To remove a specific element from a list use remove()-(element)
    or pop()-(index value)'''
#remove()
print("after remove(element)")
l1.remove(30)
print(l1)
print("remove(element)-if there are multiple same value elements (eg-20)"
      "first occurance is deleted")
l1.pop(2)
print(l1)
#pop()
print("after pop(index value)")
rem=l1.pop(2)
print("removed element",rem)
print(l1)
print("just pop() will remove the last element")
l1.pop()
print(l1)
#del list_name[index] keyword
print("del list_name[index]")
del l1[1]
print(l1)
#del l1---->this will cause an errror
#---------------------------
#clear() function
print("clear() deletes the whole list")
l1.clear()
print(l1)
