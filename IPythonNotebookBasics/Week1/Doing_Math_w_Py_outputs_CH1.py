Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hello IDLE')
Hello IDLE
>>> 1+2
3
>>> 1+3.5
4.5
>>> -1+2.5
1.5
>>> 100-45
55
>>> -1.1 + 5
3.9
>>> 3*2
6
>>> 3*2
6
>>> 3.5*1.5
5.25
>>> 3/2
1.5
>>> 4/2
2.0
>>> 3//2
1
>>> -3//2
-2
>>> 9%2
1
>>> 2**2
4
>>> 2**10
1024
>>> 1**10
1
>>> 8**(1/3)
2.0
>>> 5+5*5
30
>>> (5+5)*5
50
>>> A=3
>>> a=3
>>> a+1
4
>>> a=5
>>> a+1
6
>>> type(3)
<class 'int'>
>>> type(3.5)
<class 'float'>
>>> type(3/2)
<class 'float'>
>>> int(3.8)
3
>>> int(3.0)
3
>>> from fractions import Fraction
>>> f=Fraction(3,4)
>>> print (f)
3/4
>>> Fraction(3,4)+1+1.5
3.25
>>> Fraction(3,4)+1
Fraction(7, 4)
>>> g=Fraction(3,4)+1
>>> print (g)
7/4
>>> a=2+3j
>>> type(a)
<class 'complex'>
>>> a=complex(2,3)
>>> a
(2+3j)
>>> g
Fraction(7, 4)
>>> f
Fraction(3, 4)
>>> b=3+3j
>>> a+b
(5+6j)
>>> a-b
(-1+0j)
>>> a*b
(-3+15j)
>>> a/b
(0.8333333333333334+0.16666666666666666j)
>>> z=2+3j
>>> z.real
2.0
>>> z.imag
3.0
>>> z.conjugate()
(2-3j)
>>> (z.real**2+z.imag**2)**0.5
3.605551275463989
>>> abs(z)
3.605551275463989
>>> a = input()

>>> a=input()
1
>>> a
'1'
>>> s1='a string'
>>> s2='a string'
>>> a='1'
>>> int(a)+1
2
>>> float(a)+1
2.0
>>> int('2.0')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    int('2.0')
ValueError: invalid literal for int() with base 10: '2.0'
>>> a=float(input())
3/4
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a=float(input())
ValueError: could not convert string to float: '3/4'
>>> try:
	a=float(input('Enter a number: '))
except ValueError:
	print('You entered an invalid number')

Enter a number: 3/4
You entered an invalid number
>>> a = input('Input an integer: ')
Input an integer: 1
>>> a=int(input())
1
>>> a+1
2
>>> a=int(input())
1.0
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a=int(input())
ValueError: invalid literal for int() with base 10: '1.0'
>>> 1.1.is_integer()
False
>>> 1.0_is_integer()
SyntaxError: invalid decimal literal
>>> 1.0.is_integer()
True
>>> a=Fraction(input('Enter a fraction: '))
Enter a fraction: 3/4
>>> a
Fraction(3, 4)
>>> a=Fraction(input('Enter a fraction: '))
Enter a fraction: 3/0
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a=Fraction(input('Enter a fraction: '))
  File "C:\Users\gcamp\AppData\Local\Programs\Python\Python38\lib\fractions.py", line 178, in __new__
    raise ZeroDivisionError('Fraction(%s, 0)' % numerator)
ZeroDivisionError: Fraction(3, 0)
>>> try:
	a=Fraction(input('Enter a fraction: '))
except ZeroDivisionError:
	print('Invalid Fraction')

	
Enter a fraction: 3/0
Invalid Fraction
>>> z=complex(input('Enter a complex number: '))
Enter a complex number: 2+3j
>>> z
(2+3j)
>>> z=complex(input('Enter a complex number: '))
Enter a complex number: 2 + 3j
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    z=complex(input('Enter a complex number: '))
ValueError: complex() arg is a malformed string
>>> def is_factor(a,b):
	if b%a==0:
		return True
	else:
		return False

	
>>> is_factor(4,1024)
True
>>> for i in range(1,4)
SyntaxError: invalid syntax
>>> for i in range(1,4):
	print(i)

	
1
2
3
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in range(1,10,2):
	print(i)

	
1
3
5
7
9
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py
Your Number Please: 1
1
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py
Your Number Please: 25
1
5
25
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py
Traceback (most recent call last):
  File "D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py", line 11, in <module>
    if _name_=='_main_':
NameError: name '_name_' is not defined
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py
Traceback (most recent call last):
  File "D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py", line 11, in <module>
    if _name_ =='_main_':
NameError: name '_name_' is not defined
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py
Traceback (most recent call last):
  File "D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py", line 11, in <module>
    if _name_ == '_main_':
NameError: name '_name_' is not defined
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py
Traceback (most recent call last):
  File "D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py", line 11, in <module>
    if _name_ == '_main_':
NameError: name '_name_' is not defined
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py
Your Number Please: 1
1
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py
Traceback (most recent call last):
  File "D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py", line 11, in <module>
    if _name_ == '_main_':
NameError: name '_name_' is not defined
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py
Your Number Please: 2
1
2
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Find_Factors_of_Int.py
Your Number Please: 1
1
>>> item1 = 'apples'
>>> item2 = 'bananas'
>>> item3 = 'grapes'
>>> print('At the grocery store, I bought some {0} and {1} and {2
      
SyntaxError: EOL while scanning string literal
>>> print('At the grocery store, I bought some {0} and {1} and {2}'.format(item1,item2,item3))
At the grocery store, I bought some apples and bananas and grapes
>>> print('Number 1: {0
      
SyntaxError: EOL while scanning string literal
>>> print('Number 1: {0} Number 2: {1}'.format(1, 3.578))
Number 1: 1 Number 2: 3.578
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Multi_Table_Printer.py
Enter a number: 5
5.0 x 1=5.0
5.0 x 2=10.0
5.0 x 3=15.0
5.0 x 4=20.0
5.0 x 5=25.0
5.0 x 6=30.0
5.0 x 7=35.0
5.0 x 8=40.0
5.0 x 9=45.0
5.0 x 10=50.0
>>> '{0}'.format(1.253456)
'1.253456'
>>> '{0:.2f}'.format(1.25456)
'1.25'
>>> (25.5*2.54)/100
0.6476999999999999
>>> 650*1.609
1045.85
>>> F=98.6
>>> (F-32)*(5/9)
37.0
>>> C=37
>>> C*(9/5)+32
98.60000000000001
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Miles_and_Kilometers.py
1. Kilometers to Mile
2.Miles to Kilometers
Which conversion would you like to do?: 1
Traceback (most recent call last):
  File "D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Miles_and_Kilometers.py", line 25, in <module>
    km_mile()
NameError: name 'km_mile' is not defined
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Miles_and_Kilometers.py
1. Kilometers to Mile
2. Miles to Kilometers
Which conversion would you like to do?: 2
Enter distance in miles: 2
Traceback (most recent call last):
  File "D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Miles_and_Kilometers.py", line 28, in <module>
    miles_km()
  File "D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Miles_and_Kilometers.py", line 17, in miles_km
    km=miles*1.609
NameError: name 'miles' is not defined
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Miles_and_Kilometers.py
1. Kilometers to Mile
2. Miles to Kilometers
Which conversion would you like to do?: 2
Enter distance in miles: 100
Distance in kilometers: 160.9
>>> 
>>> x = 10 - 500 + 79
>>> x
-411
>>> 
>>> a = 1
>>> b = 2
>>> c = 1
>>> D = (b**2 - 4*a*c)**0.5
>>> x_1 = (-b + D)/(2*a)
>>> x_1
-1.0
>>> x_2 = (-b - D)/(2*a)
>>> x_2
-1.0
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Quad_eq_root_calc.py
Enter a: 1
Enter b: 2
Enter c: 1
x1: -1.0
x2: -1.0
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/Quad_eq_root_calc.py
Enter a: 1
Enter b: 1
Enter c: 1
x1: (-0.49999999999999994+0.8660254037844386j)
x2: (-0.5-0.8660254037844386j)
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Traceback (most recent call last):
  File "D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py", line 27, in <module>
    a=integer(input('Enter an integer: '))
NameError: name 'integer' is not defined
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 2
even
>>> 
>>> 
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 1
odd
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 2
even
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 2
even
19
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 2
even
2
4
6
8
10
12
14
16
18
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 2
even
24681012141618
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 2
even
2 , 4 , 6 , 8 , 10 , 12 , 14 , 16 , 18 , 
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 2
even
2 , 4 , 6 , 8 , 10 , 12 , 14 , 16 , 18 .
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 2
even
2 , 4 , 6 , 8 , 10 , 12 , 14 , 16 , Traceback (most recent call last):
  File "D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py", line 30, in <module>
    even_odd_vending_machine(a)
  File "D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py", line 26, in even_odd_vending_machine
    print(a*9+'.')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 2
even
2 , 4 , 6 , 8 , 10 , 12 , 14 , 16 , 18 .
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 7
odd
7 , 9 , 11 , 13 , 15 , 17 , 19 , 21 , 23 , 25 , 27 , 29 , 31 , 33 , 35 , 37 , 39 , 41 , 43 , 45 , 47 , 49 , 51 , 53 , 55 , 57 , 59 , 61 , 63 .
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 2
even
2 , 6 , 10 , 14 , 18 , 18 .
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 2
even
2 , 4 , 6 , 8 , 10 , 12 , 14 , 16 , 18 .
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 2
even
2 , 4 , 6 , 8 , 10 , 12 , 14 , 16 , 18 , 20 .
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 2
even
2 ,4 ,6 ,8 ,10 ,12 ,14 ,16 ,18 ,20 .
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 2
even
2 ,4 ,6 ,8 ,10 ,12 ,14 ,16 ,18 ,20 .
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 2
even
2 ,4 ,6 ,8 ,10 ,12 ,14 ,16 ,18 ,20.
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 7
odd
7 ,14 ,21 ,28 ,35 ,42 ,49 ,56 ,63 ,70.
>>> 
= RESTART: D:/Git/MS_DS_CUNY_SPS/IPythonNotebookBasics/Week1/DMwP_Challenge_1.1.py
Enter an integer: 9
odd
9 ,18 ,27 ,36 ,45 ,54 ,63 ,72 ,81 ,90.
>>> 