Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> simplelist = [1,2,3]
>>> simplelist[0]
1
>>> simplelist[1]
2
>>> simplelist[2]
3
>>> stringlist = ['a string', 'b string', 'c string']
>>> stringlist[0]
'a string'
>>> stringlist[1]
'b string'
>>> stringlist[2]
'c string'
>>>  >
 
SyntaxError: unexpected indent
>>> emptylist=[]
>>> emptylist
[]
>>> emptylist.append(1)
>>> emptylist
[1]
>>> emptylist.append(2)
>>> emptylist
[1, 2]
>>> simpletuple = (1, 2, 3)
>>> simpletuple[0]
1
>>> simpletuple[1]
2
>>> simpletuple[2]
3
>>> simplelist[-1]
3
>>> simpletuple[-1]
3
>>> l = [1, 2, 3]
>>> for item in 1:
	print(item)

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    for item in 1:
TypeError: 'int' object is not iterable
>>> l = [1, 2, 3]
>>> for item in l:
 print(item)

 
1
2
3
>>> k = [1, 2, 3]
>>> for item in k:
	print(item)

	
1
2
3
>>> l=[1,2,3]
>>> for index, item in enumerate(1):
	print(index, item)

	
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    for index, item in enumerate(1):
TypeError: 'int' object is not iterable
>>> for index, item in enumerate(l):
	print(index, item)

	
0 1
1 2
2 3
>>> x_numbers = [1, 2, 3]
>>> y_numbers = [2, 4, 6]
>>> from pylab import plot, show
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    from pylab import plot, show
ModuleNotFoundError: No module named 'pylab'
>>> from pylab import plot, show
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    from pylab import plot, show
ModuleNotFoundError: No module named 'pylab'
>>> 
>>> 
>>> from pylab import plot, show
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    from pylab import plot, show
ModuleNotFoundError: No module named 'pylab'
>>> 