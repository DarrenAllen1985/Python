#list brackets starts with these[]
#List are mutable tuples are immutable
#Sets doesnt take any duplicates

#Accessing a the list
courses = ['History','Math','Physics','CompSci']
print(courses)

print("--------")


#Getting the lenght of the list
courses = ['History','Math','Physics','CompSci']
print('The lenght of the list is : ',len(courses))

print("--------")

#Getting a specific value in a list
courses = ['History','Math','Physics','CompSci']
print('The specific value in a list : ',courses[2])
print('negative -1 will get the last item in a list : ',courses[-1])

print("--------")
#Getting values between a range [0:2] = History,Math
courses = ['History','Math','Physics','CompSci']
print('Between a range [0:2]: ',courses[0:2])
print("--------")

#Adding item to our list
courses = ['History','Math','Physics','CompSci']
courses.append('Art')
print('Check wheres art',courses)
courses.remove('Art')

print("--------")

#Adding to a specific locations to a list
courses = ['History','Math','Physics','CompSci']
courses.insert(0,'Art')
print('Check wheres art',courses)
courses.remove('Art')

print("--------")

#Adding multiple values to the list
courses = ['History','Math','Physics','CompSci']
courses_2 = ['Art','Education']
courses.insert(0,courses_2)
print(courses)
courses.remove(courses_2)
print(courses)

print("--------")
#Adding multiple values to the list 2
courses = ['History','Math','Physics','CompSci']
courses_2 = ['Art','Education']
courses.extend(courses_2)
print(courses)

#Removing values from our list
courses = ['History','Math','Physics','CompSci']
print(courses)
courses.remove('Math')
print(courses)

#Removing the last value from our list
courses = ['History','Math','Physics','CompSci']
print(courses)
popped = courses.pop()
print(popped)
print(courses)

#Sorting a list
courses = ['History','Math','Physics','CompSci']
print(courses)
courses.reverse()
print(courses)
courses.sort()
print(courses)

nums = [1,5,2,4,3]
nums.sort()
print(nums)
#reverse sort
nums.sort(reverse= True)
print(nums)

#Sorted function if you dont want to sort the original list
courses = ['History','Math','Physics','CompSci']
sorted_courses = sorted(courses)
print(sorted_courses)

#Minimum value
nums = [1,5,2,4,3]
print(min(nums))

#Maximum value
nums = [1,5,2,4,3]
print(max(nums))

#sum value
nums = [1,5,2,4,3]
print(sum(nums))

#finding the index of the list
courses = ['History','Math','Physics','CompSci']
print(courses.index('Physics'))

#finding the value un the list
courses = ['History','Math','Physics','CompSci']
print('Math' in courses)

#Looping through i list
courses = ['History','Math','Physics','CompSci']
for Indx in courses:
    print(Indx)

#Looping and printing indx and value
courses = ['History','Math','Physics','CompSci']
for Index,course in enumerate(courses):
    print(Index,course)

#Joining a stringa in a list
courses = ['History','Math','Physics','CompSci']
course_Str = ' - '.join(courses)
newlist = course_Str.split(' - ')
print(course_Str)
print(newlist)

######################################################tupples##########
#Mutable
list_1 = ['History','Math','Physics','CompSci']
list_2 =list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'
print(list_1)
print(list_2)

#Immutable
tuple_1 = ('History','Math','Physics','CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'
print(tuple_1)
print(tuple_2)

#Sets removes duplicates automatically
cs_courses = {'History','Math','Physics','CompSci'}
print(cs_courses)