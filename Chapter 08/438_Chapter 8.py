# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ENrsVu56pwd6gq5zbaWauCkb1RZ4t8ix
"""

# Creating a String

# 1.	>>> print("hello")
# 2.	>>> print('hello')
# 3.	>>> print("doesn't")
# 4.	>>>print('He said "Hello"')

# Accessing Values in a String

# 1.	>>> a="hello world"
# 2.	>>>a[0]
# 3.	>>>a[2: ]
# 4.	>>>a[ : ]
# 5.	>>>a[ :6]
# 6.	>>>a[3:8]
# 7.	>>>a[6:-3]
# 8.	>>> a[::−1]                            # Reversing items 
# 9.	>>>a[0:10:2]                       # Skipping items

# Changing or deleting a string

# 1.	>>> a="hello"
# 2.	>>>a[4]='a'
# 3.	Traceback (most recent call last):
# 4.	  File "<pyshell#17>", line 1, in <module>
# 5.	a[4]='a'
# 6.	TypeError: 'str' object does not support item assignment
# 7.	>>> a="world"
# 8.	>>> a
# 9.	      'world'

# >>> del a[3]
# 2.	Traceback (most recent call last):
# 3.	  File "<pyshell#20>", line 1, in <module>
# 4.	    del a[3]
# 5.	TypeError: 'str' object doesn't support item deletion
# 6.	>>> del a
# 7.	>>> a
# 8.	Traceback (most recent call last):
# 9.	  File "<pyshell#22>", line 1, in <module>
# 10.	    a
# 11.	NameError: name 'a' is not defined

# Concatenation

# 1.	>>> a="hello"
# 2.	>>> b="world"
# 3.	>>> c=a+b
# 4.	>>> c
# 5.	'helloworld'

# Repetition

# 1.	a="hello "
# 2.	b=a*4
# 3.	b
# 4.	'hello hellohellohello

# Membership

# 1.	a="hello world"
# 2.	b="world"
# 3.	c="word"
# 4.	b in a
# 5.	True
# 6.	c in a
# 7.	False
# 8.	b not in a
# 9.	False

# Raw String

# 1.	>>> print("hello\nworld")
# 2.	hello
# 3.	world
# 4.	>>>print("hello" r "\nworld")
# 5.	hello\nworld

# String formatting

# 1.	>>> '%s, %s, %f' %(23,"hello",2.13)
# 2.	'23, hello, 2.130000'
# 3.	>>> '{0},{1},{2:f}'.format(23,"hello",2.13)
# 4.	'23,hello,2.130000'

# Triple Quote Code

# 1.	>>>print("""hello
# 2.	how're you!!!
# 3.	I am good""")
# 4.	
# 5.	hello
# 6.	how're you!!!
# 7.	I am good

# String capitalize() Method

# 1.	>>> a=”hello world”
# 2.	>>>a.capitalize()
# 3.	'Hello world'

# String center() Method

# 1.	>>> a="hello world"
# 2.	>>>a.center(30,'*')
# 3.	'*********hello world**********'

# String count() Method

# 1.	>>> a="hello world hello"
# 2.	>>> sub='lo'
# 3.	>>>a.count(sub,3)
# 4.	2

# String decode() Method

# 1.	String = ‘Python’
# 2.	Print(‘The string is:’, String)
# 3.	String_utf=String.encode()
# 4.	Print(‘The encoded version is:’,String_utf)
# 5.	Print(‘The decode version is:’,String_utf.decode())

# String encode() method

# 1.	String = ‘Python’
# 2.	Print(‘The string is:’, String)
# 3.	String_utf=String.encode()
# 4.	Print(‘The encoded version is:’,String_utf)

# String endswith() method

# 1.	Str='this is a test of endswithfuction....!!' 
# 2.	suffix='!!' 
# 3.	print (Str.endswith(suffix)) 
# 4.	print (Str.endswith(suffix,25)) 
# 5.	suffix='exam' 
# 6.	print (Str.endswith(suffix)) 
# 7.	print (Str.endswith(suffix, 0, 24))

# String expandtabs() method

# 1.	str = "this is expandtabsfunction....!!" 
# 2.	print ("Original string: " + str) 
# 3.	print ("Defaultexapanded tab: " +  str.expandtabs()) 
# 4.	print ("Double exapanded tab: " +  str.expandtabs(16))

# String find() method

# 1.	str1 = "this is string find function..!!" 
# 2.	str2 = "find"; 
# 3.	print (str1.find(str2)) 
# 4.	print (str1.find(str2, 10)) 
# 5.	print (str1.find(str2, 40))

# String index() method

# 1.	str1 = "this is string index function...!!" 
# 2.	str2 = "index"; 
# 3.	print (str1.index(str2)) 
# 4.	print (str1.index(str2, 10))

# String isalnum() method

# 1.	str = "thisisnot1234" 
# 2.	print (str.isalnum()) 
# 3.	str = "this is string alphanumfunction..!!" 
# 4.	print (str.isalnum())

# String isalpha() method

# 1.	str = "thisisastring";
# 2.	print (str.isalpha()) 
# 3.	str = "this is string isalphafunction..!!" 
# 4.	print (str.isalpha())

# String islower() method

# 1.	str = "THIS is string islowerfunction..!!" 
# 2.	print (str.islower()) 
# 3.	str = "this is string islowerfunction..!!" 
# 4.	print (str.islower())

# String isnumeric() method:

# 1.	str = "this2016"   
# 2.	print (str.isnumeric()) 
# 3.	str = "23443434"
# 4.	print (str.isnumeric())

# String isspace() method:

# 1.	str = "       "  
# 2.	print (str.isspace()) 
# 3.	str = "This is string isspace function!!" 
# 4.	print (str.isspace())

# String istitle() method:

# str = "This Is String Function..!!" 
# print (str.istitle()) 
# str = "This is string function..!!" 
# print (str.istitle())

# String isupper() method

# 1.	str = "THIS IS STRING ISUPPER FUNCTION..!!" 
# 2.	print (str.isupper()) 
# 3.	str = "THIS is string upper function..!!" 
# 4.	print (str.isupper())

# String join() method:

# 1.	s = ">" 
# 2.	seq = ("3", "2", "1") # This is sequence of strings. 
# 3.	print (s.join( seq ))

# String len() method

# 1.	str = "This Is String lenFunction..!!" 
# 2.	print ("Length of the string: ", len(str))

# String ljust() method:

# 1.	str = "This Is String ljustFunction..!!" 
# 2.	print (str.ljust(50, '*'))

# String lower() method:

# 1.	str = "This Is String lower Function..!!" 
# 2.	print (str.lower())

# String lstrip() method:

# 1.	str = "This Is String lstripFunction..!!" 
# 2.	print (str.lstrip())
# 3.	str = "*****this is string lstripfunction..!!*****" 
# 4.	print (str.lstrip('*'))

# String maketrans() method

# 1.	Intab=”aeiou”
# 2.	outtab = "12345" 
# 3.	trantab = str.maketrans(intab, outtab) 
# 4.	str = "this is string translate function...!!" 
# 5.	print (str.translate(trantab))

# String max() method

# 1.	str = "this is a string example..!!" 
# 2.	print ("Max character: " + max(str)) 
# 3.	str = "this is a string max function..!!" 
# 4.	print ("Max character: " + max(str))

# String min() method

# 1.	str = "thisisastringexample..!!" 
# 2.	print ("Min character: " + min(str)) 
# 3.	str = "thisisastringmaxfunction..!!" 
# 4.	print ("Min character: " + min(str))

# String replace() method

# 1.	str = "this is a replace function" 
# 2.	print (str.replace("is", "was"))

# String rfind() method

# 1.	str1 = "this is a string rfindfunction..!!" 
# 2.	str2 = "is" 
# 3.	print (str1.rfind(str2)) 
# 4.	print (str1.rfind(str2, 0, 10)) 
# 5.	print (str1.rfind(str2, 10, 0)) 
# 6.	print (str1.find(str2)) 
# 7.	print (str1.find(str2, 0, 10)) 
# 8.	print (str1.find(str2, 10, 0))

# String rindex() method

# 1.	str1 = "this is a string rindex function...!!" 
# 2.	str2 = "is" 
# 3.	print (str1.rindex(str2)) 
# 4.	print (str1.rindex(str2,10))

# String rjust() method

# 1.	str = "this is string rjustfunction..!!" 
# 2.	print (str.rjust(50, '*'))

# String rstrip() method

# 1.	str = "     this is a string rstripfunction....!!     " 
# 2.	print (str.rstrip())

# String split() method

# 1.	str = "this is a string split function..!!" 
# 2.	print (str.split( )) 
# 3.	print (str.split('i',1)) 
# 4.	print (str.split('l'))

# String  splitlines() method

# 1.	str = "this is \nstringsplitlines \nfunction..!!"

# String startswith() method

# 1.	str = "this is string startswithfunction....!!" 
# 2.	print (str.startswith( 'this' )) 
# 3.	print (str.startswith( 'string', 8 )) 
# 4.	print (str.startswith( 'this', 2, 4 ))

# String strip() method

# 1.	str = "*****this is a string strip function....!!*****" 
# 2.	print (str.strip( '*' ))

# String swapcase() method

# 1.	str = "this is string swapcasefunction....!!" 
# 2.	print (str.swapcase()) 
# 3.	str = "This Is String Swapcase Function….!!" 
# 4.	print (str.swapcase())

# String title() method

# 1.	str = "this is string title function....!!" 
# 2.	print (str.title())

# String translate() method 

# 1.	from string import maketrans   # Required to call maketrans function. 
# 2.	input = "aeiou" 
# 3.	output = "12345" 
# 4.	traslt = maketrans(input, output) 
# 5.	str = "this is string example....wow!!!"; 
# 6.	print (str.translate(traslt))

# String upper() method

# 1.	str = "this is string upper function....!!" 
# 2.	print ("str.upper : ",str.upper())

# String zfill() method

# 1.	str = "this is string zfill function...!!" 
# 2.	print ("str.zfill : ",str.zfill(40))

# String isdecimal() method

# 1.	str = "thisisnot01234" 
# 2.	print (str.isdecimal()) 
# 3.	str = "2334567434" 
# 4.	print (str.isdecimal())

# Programs:
# Program to find the index of a character in a string
# 2.	a=input("Enter a string")
# 3.	b=input("Enter a character")
# 4.	pos=-1
# 5.	for i in range(len(a)):
# 6.	    if(a[i]==b):
# 7.	pos=i
# 8.	if(pos!=-1):
# 9.	print("character found at index",pos)
# 10.	else:
# 11.	print("character not found")

# Program that counts the number of characters in a string
# 1.	str=input('Enter a string: ')s
# 2.	count=0
# 3.	for i in str:
# 4.	    for j in str:
# 5.	        if j is i:
# 6.	            count=count+1
# 7.	    print(i,count)
# 8.	    count=0

# Program to reverse a string
# 1.	a=input("Enter a string: ")
# 2.	l=len(a)
# 3.	rev=""
# 4.	for i in a:
# 5.	    rev=rev+a[l-1]
# 6.	    l=l-1
# 7.	print(rev)

# Program to find a substring in the string
# 1.	a=input("enter a string: ")
# 2.	s=input("enter substring: ")
# 3.	ans=a.find(s)
# 4.	p=ans+len(s)
# 5.	if(ans!=-1) and a[ans-1]==" " and a[p]==" ":
# 6.	    print("found")
# 7.	else:
# 8.	print("not found")

# Program to count vowels in a string
# 1.	str=input('Enter a string: ')
# 2.	count=0
# 3.	for i in str:
# 4.	if( (i is 'a') or (i is 'e') or (i is 'i') or (i is 'o') or (i is 'u')):
# 5.	        count=count+1
# 6.	print(count)

# Program to check whether a string is palindrome or not
# 7.	a=input("enter a string: ")
# 8.	a=str.upper(a)
# 9.	b=""
# 10.	for i in a:
# 11.	    b=i+b
# 12.	if(b==a):
# 13.	    print("palindrome")
# 14.	else:
# 15.	print("not palindrome")

# Program to find the occurrence of a word in a string
# 1.	s1=input("enter a string: ")
# 2.	word=input("enter word")
# 3.	s2=[]
# 4.	count=0
# 5.	s2=s1.split(" ")
# 6.	for i in range(0,len(s2)):
# 7.	    if(word==s2[i]):
# 8.	        count+=1
# 9.	print("count of word is ",count)

# Program to sort a string
# 1.	a=input("Enter a string")
# 2.	b=a.split( )
# 3.	b.sort()
# 4.	print(b)

# Program to check whether the two strings are anagram or not
# 1.	# check whether strings are anagram or not
# 2.	s1=input("enter first string: ")
# 3.	s2=input("enter second string: ")
# 4.	if(sorted(s1)==sorted(s2)):
# 5.	print("both strings are anagram")
# 6.	else:
# 7.	print("strings are not anagram")

# Program to calculate the number of digits and characters in a string
# 1.	s1=input("enter a string: ")
# 2.	countN=0
# 3.	countC=0
# 4.	for i in s1:
# 5.	    if(i.isdigit()):
# 6.	countN+=1
# 7.	countC+=1
# 8.	print("digits = ",countN)
# 9.	print("characters = ",countC)