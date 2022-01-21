### Basic Syntax
- Just as in case of a natural language, computer programming language comprises of a set of predefined words which are called keywords. Usage of each keyword has a well defined in the form of syntax. Programmer uses these keywords in the source code to develop programming logic.

- Python 3.x has 33 keywords defined in it. Since they have a predefined meaning attached to them, they cannot be used for any other purpose. List of Python keywords can be obtained using help(“keywords”) command.
```
In  [1] :help ("keywords") 
Out [1] : 
False               def if                  raise
None                del import              return
True                elif in                  try
and                 else is                  while
as                  except lambda              with
assert              finally nonlocal            yield
break               for not                 
class               from or                  
continue            global pass
```
#### Identifier:
- In addition to keywords, there are various other elements in a Python program. They are called identifiers. A program can have keywords, variables, functions, classes, modules, packages etc. An identifier should start with either an alphabet (lower or upper case) or underscore (_). More than one alpha-numeric characters or underscores may follow.

    - Keywords are predefined. They are in lowercase. They can’t be used for any other purpose.
    - Conventionally, name of class begins with uppercase alphabet. Others start with lowercase alphabet.
    - Single underscore in the beginning of a variable name is used to indicate a private variable.
    - Two underscores in beginning indicate that the variable is strongly private.
    - Two leading and trailing underscores are used in language itself for special purpose. For example (e.g. __add__, __init__)
Here are some examples of valid identifiers:
```
Student	score	aTotal	sum_age	__count	__init__	TotalValue	price1	cost_of_item
```
However, these phrases are invalid identifiers
```
1234	sum of age	phy+che	TotalVal/3	cost-of-item
```
Identifiers are case sensitive. Hence age and Age cannot be used interchangeably.

#### Statements:
- Any text terminated by Enter key (called newline character) is recognized as a statement by Python interpreter. Hence, each line in the input cell of notebook is a statement. Occasionally, a Python statement may spill over multiple lines. To do so, use backslash (\) as continuation character.
```
In  [2] : greeting="Hello World. \
            Welcome to the exciting world \
            of Python programming"
            greeting
Out [2] : 'Hello World. Welcome to the exciting world of Python programming'
```
- However, if number of elements in other data types such list, tuple or dictionary spread over many lines, there is no need to use backslash to show continuation.
```
In  [3] : numbers=[10, 20, 30, 40,
                             50, 60, 70, 80,90, 100]
            numbers
Out [3] :[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```
- n the other hand, to write more than one statements in single line, use semicolon (;) to separate them.
```
In  [4]:a=10; b=20; c=a+b; print (c)
Out [4] :30
```
###### Indents

- Multiple statements are usually grouped together to define a function, class or loop. Python uses mechanism of uniformly indented statements to denote such a group or block. Usually a colon (:) symbol marks the beginning of block.

- When you press Enter key after colon mark, next line starts after leaving a white space from left margin – something similar to pressing Tab key. Every subsequent statement in the block follows same indent level. To mark end of the block, press the backspace and reduce the indentation level  back to earlier level.

- Look at the code snippet in the input cell. The code itself may not be understood at this level but don’t worry. Just see how indent level increases after colon symbol.
```
In  [5] :num=int(input("enter a number"))
    l=len(num)
    app=0
    for i in range(l):
        f=int(num[i])
        if app==0:
                app=app+1
                if i==0 : s=f
        else:
                if app>0:
                        if s==f:
                                app=app+1
                        else:
                                print (s,app)
                                app=1
                                s=f
print (s,app)
```
Here is another example of definition of a class. Again don’t bother what the code is about. Just see how indentation level increases after each colon symbol.
```
In  [6]:class car:
        def __init__(self):
                self.__speed=40
        @property
        def speed(self):
                return self.__speed
        @speed.setter
        def speed(self, x):
                self.__speed=x  
```
##### Comments

Extensive use of comments in program’s source code is considered to be a good habit. A comment is some description or explanatory text within the program. Such a descriptive text is not executed by language interpreter. However it is extremely useful for programmer and other collaborators to understand or recollect the logic, syntax and usage.

Any line beginning with # symbol is treated as comment and ignored by Python. Its effect lasts till a new line is initiated by enter key. If # symbol appears after a valid expression, remainder of line is considered as comment.
```
In  [7]
:
#program to calculate area. (This is a comment)
l=100
b=200
a=l*b # formula for area (This is also comment but after expression)
print (a)
```
You can also mark lines in input cell of notebook as comment. Select one or more lines and press Ctrl and /. Selected lines will now have # symbol in the beginning.
Multiple lines between triple inverted comma symbols (''' or """) is also treated as comment if it is not a docstring of a function or class. (What is a docstring? You will come to know in chapter on Functions)
```
In  [8]
:
'''
comment1
comment2
comment3
'''
x=10
y=20
print (x+y)
```
