# -*- coding: utf-8 -*-
"""Python_lab1CS0121.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HF9NQqnGTAoJd3y4G_8ZAiWC429IAUad

# Python Programming basics

## Types and Functions

Extend the function to take an optional 3rd argument.

Extend the function to take another optional flag parameter and add only if it is true
"""

def add(x,y):
    return x + y

def add(x, y, z):
  return x+y+z

def add(x, y, z, flag=None):

     if (flag==True):
        return add(x,y,z)


print(add(1,1,2,True))

"""Assign a function to a variable 'a' and print the output"""

def add(x,y):
  return x+y

a = add
print(a(2,3))

"""## Iterations in python

Create a list of 5 elements

Square every item in the list using a loop inside the array index

Show how to use a iterator. First, use enumerate to create a new tuple from above list
"""

li=[1,2,3,4,5]                    #squaring
for i in range(len(li)):
  li[i]=li[i]*li[i]
print(li)


it=iter(li)                    #iterator
print(next(it))
print(next(it))


obj1=enumerate(li,10)

                       # first use enumerate then created a new tuple from above li
print(tuple(obj1))
tuple(li)
print(tuple(li))

#use of a iterator
#iterator- returns numbers that starts with 25 and each and every time it is passed it gets squared.

class MyInit:    #for initialization
  def __iter__(self):
    return self

  def __next__(self):  # does the operation
    a = self.a
    return x

obj1 = MyInit()
itr = iter(obj1)

print(next(itr))

#First, use enumerate to create a new tuple from above list
listSequence = ["eat","sleep","repeat"]
obj2=enumerate(listSequence)
print(tuple(obj2))
tup=()
#at first Enumerating thro' the list and then iterating thro' the loop with for loop.
for index,value in enumerate(listsequence):

print(tup)

"""Now use a zip iterator to do the same.

Now state the differences between a zip and enumerate iterator.

Python`enumerate()` and `zip()` are built-in functions that can be used on sequences.

`enumerate()` function can be use to iterate over indices and items of a list.

`zip()` function make an iterator that aggregates elements from each of the iterables. In simple words it can be used to iterate over two or more lists in parallel.

## Strings in Python

Open the file poem.txt and print lenght of each line.

Find sum of each line, mean, median and standard deviation of all lines in the file.

Count the number of words in the file

Print the first 1000 characters from poem.txt.

Print the 3rd to 5th words from the file.
"""

with open('poem.txt','r') as file:


    for line in file:
        print(line)

        li.append(len(line))

    print(li)

import statistics
print(sum(li))
print(statistics.mean(li))
print(statistics.median(li))
print(statistics.stdev(li))

with open('poem.txt','r') as file:
  words=file.read().split()

from google.colab import drive
drive.mount('/content/drive')

with open('poem.txt','r') as file:
  words=file.read().split()
  print(words[2:5])

"""Get every third word between the second and the 15th words from poem.txt.

Print the last word from the file and change the second last characted in the string to 'g'.

State if the above operation completed successfully. State reasons

# Find types of Python variables and functions

Find what are the types of the following and state if they are mutable of immutable
"""

None
1
1.0
#add    on only taking add this is showing error that add is not defined so we must
        #first define by giving a value or making function
(1,'a',3,'b')
a=[1,'a',3,'b']
print(type(None))
print(type(1))
print(type(1.0))

print(type((1,'a',3,'b')))
print(type([1,'a',3,'b']))

"""Append new elements at the end of a list"""

a.append(4)
print(a)

"""Loop through each element of the list"""

for i in range (len(a)):
  print(a[i])

"""Use a indexing operator"""

#indexing operator
str_indexing = ""
print(lastchar)

"""Concatenate two lists"""

a=[1,2,3,4,5]
b=[6,7,8,9,10]

a.extend(b)# if we use append then it joins whole list b as single entity to a
print(a)

"""Use * to repeat lists"""

c=a*2
print(c)

"""Use the in operator to check if something is in a list"""

if 11 in a:
  print("yes")
else:
  print("no")

"""Initialize a string and slice the first 1, 2 and 3 characters. Then from 3rd to end."""

name='rohan'
print(name[0:1])
print(name[0:2])
print(name[0:3])
print(name[2:])

"""Take a first name and a last name and then concatenate the last name with 3 times the first name and show result."""

first_name='rohan'
last_name='raj'
full_name=last_name+first_name*3
print(full_name)

"""Take a string with four words. Use the split function to display the second and the last words"""

sentence="hello machine learning world"
words=sentence.split()
print(words[1])
print(words[-1])

"""Concatenate a number with a string. Update following:"""

roll=2315010
name="rohan"
name=name+str(roll)
print(name)

"""## Dictionaries associated with lists

Create a list of keys and values
"""

dictionary={'rohan':2315010,'manvendra':2315048,'ashutosh':2315048}
print(dictionary)

"""Iterate over all the keys"""

print(dictionary.keys())

"""Iterate over all the values"""

print(dictionary.values())

"""Iterate over all the key-value pairs in the list"""

print(dictionary.items())

"""Unpack the following sequence into different variables"""

a=('Prithwish','IIITG','prithwish.sen@iiitg','CSE')
name,college_name,email,branch=a
print(name)
print(college_name)
print(email)
print(branch)

"""Use Python's in-built methods for string formatting"""

sales_record = {
'price': 3.24,
'num_items': 4,
'person': 'Prithwish'}

sales_statement = '{} got {} item(s) at a cost of {} each for a total of {}'

"""Take a list of 10 elements and convert into json using  json library. Demonstrate use of loads and dumps"""

import json
a=list(range(10))
b=json.dumps(a)
print(b)
print(type(b))
c=json.loads(b)
print(c)
print(type(c))

"""# Python objects and functions

Take the following code:
"""

class students:
    dept = "Department of CSE"
    def assign_name(self, n):
        self.name = n
    def assign_location(self, l):
        self.location = l

"""Create a object of the class above. Set name and location of your choice."""

s1=students()
s1.assign_name('Dip Shankar')
s1.assign_location('GuwahatI,Asaam,India')

"""Format accordingly and print in a manner so we see something like : "Dip Sankar lives in Guwahati, Assam, India and works in the Department of CSE". The name and location should be of your choice. Use 1 print only"""

sentence = ('{} lives in {} and works in the {}'.format(s1.name,s1.location,students.dept))
print(sentence)

"""Create two lists of 5 elements each. Map the min function to the lists using map(). Print the minimum object."""

li1=[1,2,4,5,8]
li2=[2,1,3,6,9]
def min(a,b):
  if(a>b):
    return b
  else:
    return a
li3=list(map(min,li1,li2))
print(li3)

"""Iterate through that object and print the elements.

# Working with CSV

Let's import a file with fuel economy data
"""

import csv
with open('mpg.csv','r') as file:
  mpg=list(file)

"""Find out how many items are there in the dictionary"""



for item in mpg[1].items():

"""Find the column names with keys"""



"""Find the average cty fuel economy across all cars. All values in the dictionaries are strings."""



"""Find the average hwy fuel economy across all cars"""



"""Use set to return the unique values for the number of cylinders the cars."""

cylinders = set(d['cyl'])

"""Group the cars by number of cylinder, and finding the average cty mpg for each group."""

MpgByCyl = []

for c in cylinders: # iterate over all the cylinder levels
    summpg =
    typecount =
    for d in mpg: # iterate over all dictionaries
        if d['cyl'] == c:

MpgByCyl.sort(key=lambda)
MpgByCyl

"""Return the unique values for the class types in our dataset using set."""

vehicleclass = set(d['class'] for d in mpg)

"""Find average miles per gallon in the highway for each class of vehicles"""

MileageByClass = []

for t in : # iterate over all the vehicle classes
    sumpg = 0
    classCount = 0
    for d in mpg:
        if d['class'] == t:
    MileageByClass.append((t, ))

MileageByClass.sort(key=lambda x: x[1])