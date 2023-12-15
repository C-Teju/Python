#Dictionary
d1={'name':'akash', 'age':25,'status':'Pass'}
print(d1)
d2={'name':'Priya', 'age':23,'status':'Fail'}
print(d2)

#duplicate key:value pairs are not allowed
'''d1={'name':'akash','name':'akash', 'age':25,'status':'Pass'}'''

#duplicate values are allowed for different keys
d1={'name':'akash','name1':'akash', 'age':25,'status':'Pass'}
print(d1)

#duplicate keys are not allowed 
d1={'name':'akash','name':'Priya', 'age':25,'status':'Pass'}
print(d1)


#update
d1.update(d2)
print(d1)
print(d2)

#to display all values from the list
students={'s1':'akash','s2':'Priya','s3':'Arjun'}
print(students.values())

#to display all keys from the list
students={'s1':'akash','s2':'Priya','s3':'Arjun'}
print(students.keys())

#to display all items from the list
students={'s1':'akash','s2':'Priya','s3':'Arjun'}
print(students.items())
