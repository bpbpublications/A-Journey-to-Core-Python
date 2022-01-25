# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FDLjvGBfy6xYYuDtZmrQP6rIylzkFOKJ
"""

# Creating a Tuple

# 1.	t1=(1,3,'hello',98.4,76)
# 2.	t4='a','f',43
# 3.	t=tuple('hello')
# 4.	t
# 5.	('h', 'e', 'l', 'l', 'o')
# 6.	t2=()                            #empty tuple
# 7.	t3=tuple()                  #empty tuple

# Accessing Values in Tuples

# 1.	t=(23,'hello',56.8,90,'python')
# 2.	print(t[2])
# 3.	56.8
# 4.	print(t[1:3])
# 5.	('hello', 56.8)

# Updating Tuples 

# 1.	t1=(65,90,89.7,'abc',78)
# 2.	t1[3]=88
# 3.	Traceback (most recent call last):
# 4.	  File "<pyshell#50>", line 1, in <module>
# 5.	    t1[3]=88
# 6.	TypeError: 'tuple' object does not support item assignment
# 7.	t2=(78,98)
# 8.	t1=t1+t2
# 9.	print(t1)
# 10.	(65, 90, 89.7, 'abc', 78, 78, 98)

# Deleting Tuple Elements

# 1.	t=(23,'hello',56.8,90,'python')
# 2.	del t[2]
# 3.	Traceback (most recent call last):
# 4.	  File "<pyshell#55>", line 1, in <module>
# 5.	    del t[2]
# 6.	TypeError: 'tuple' object doesn't support item deletion
# 7.	del(t)
# 8.	t
# 9.	Traceback (most recent call last):
# 10.	  File "<pyshell#57>", line 1, in <module>
# 11.	    t
# 12.	NameError: name 't' is not defined

# Len

# 1.	t=(12,45,'abc',67.5,'def',5)
# 2.	len(t)
# 3.	6

# Concatenation

# 1.	a=(1,2,3)
# 2.	b=('abc','def','xyz')
# 3.	a+b
# 4.	(1, 2, 3, 'abc', 'def', 'xyz')

# Repetition 
# 1.	a=(12,'abc',56.6)
# 2.	print(a*3)

# Membership

# 1.	t1=('h','e','l','l','o')
# 2.	t2=('w','o','r','l','d')
# 3.	 'h' in t1
# 4.	True
# 5.	'h' in t2
# 6.	False
# 7.	'e' not in t1
# 8.	False
# 9.	'e' not in t2
# 10.	True

# Iteration

# 1.	for x in (1,2,3) :
# 2.	 print (x, end=' ')
# 3.	1 2 3

# Indexing, Slicing and Matrixes

# 1.	t=('abc',45,90,45.6,'xyz',12.2,'mno')
# 2.	t[2]
# 3.	90
# 4.	t[4]
# 5.	'xyz'
# 6.	 t[2:4]
# 7.	(90, 45.6)
# 8.	t[4:]
# 9.	('xyz', 12.2, 'mno')
# 10.	[-3]
# 11.	'xyz'
# 12.	t[-3:]
# 13.	('xyz', 12.2, 'mno')

# Tuple len() method

# 1.	tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc') 
# 2.	print ("First tuple length : ", len(tuple1)) 
# 3.	print ("Second tuple length : ", len(tuple2))

# Tuple max() method 

# 1.	tuple1, tuple2 = ('maths', 'che', 'phy', 'bio'), (456, 700, 200) 
# 2.	print ("Max value element : ", max(tuple1)) 
# 3.	print ("Max value element : ", max(tuple2))

# Tuple min() method 

# 1.	tuple1, tuple2 = ('cpp', 'php', 'java', 'python'), (754, 600, 100) 
# 2.	print ("min value element : ", min(tuple1)) 
# 3.	print ("min value element : ", min(tuple2))

# Tuple tuple() method

# 1.	list1= ['maths', 'che', 'phy', 'bio'] 
# 2.	tuple1=tuple(list1) 
# 3.	print ("tuple elements : ", tuple1)

# Programs

# 1.	Program to remove all tuples in a list of tuples with the USN outside the given range.
# 2.	y=[('a','12CS117'),('b','12CS149'),('c','12CS260'),('d','12CS295'),('e','12CS325')]
# 3.	low=int(input("Enter lower range (starting with 12CS): "))
# 4.	up=int(input("Enter upper range (starting with 12CS): "))
# 5.	l='12CS'+str(low)
# 6.	u='12CS'+str(up)
# 7.	for i in y:
# 8.	    if i[1]>=l and i[1]<=u:
# 9.	        print(i)

# Program to sort a list of tuples in increasing order by the last element in each tuple.
# 1.	def last(n):
# 2.	 return n[pos]
# 3.	def sort(tuples):
# 4.	 return sorted(tuples,key=last)
# 5.	a=[(12,34),(22,45),(23,12),(20,10),(45,67)]
# 6.	pos=1
# 7.	print("Sorted: ")
# 8.	print(sort(a))

# Program to create a list of tuples with the first element as the number and the second as the square of the number.
# 1.	l_r=int(input("Enter the lower range: "))
# 2.	u_r=int(input("Enter the upper range: "))
# 3.	tuple=[(x,x**2) for x in range(l_r,u_r+1)]
# 4.	print(tuple)