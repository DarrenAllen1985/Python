#Dictionary
student = {"name": 'John' ,'age': 25,'courses': ['Math', 'CompSci']}
print(student)

#retrieving one key of a dictionary
student = {"name": 'John' ,'age': 25,'courses': ['Math', 'CompSci']}
print(student['name'])

#update a string
student = {"name": 'John' ,'age': 25,'courses': ['Math', 'CompSci']}
student.update({'name': 'Jane','age': 26,'phone': '555-5555'  })
print(student)


#Looping throught a dictionary
spam = {'color':'red','age':42}
for v in spam.values():
    print(v)

#Getting the keys from a Dictionary
spam = {'color':'red','age':42}
for k in spam.keys():
    print(k)

#Printing items in a dict
spam = {'color':'red','age':42}  
for i in spam.items():
    print(i)

#True list of the dictionary
spam = {'color':'red','age':42}
for k,v in spam.items():
    print('Key: '+ k + ' Value : '+ str(v))

#Adding a value in a Dict
spam = {'name':'Pooka','age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
print(spam)

#####pretty print import ####
import pprint
count={}
message = 'It was a bright cold day in April, and tge clocks were striking thirteen.'
for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1
    print(character)
pprint.pprint(count)