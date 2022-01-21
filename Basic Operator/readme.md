### Basic Operator
Python Operators in general are used to perform operations on values and variables. These are standard symbols used for the purpose of logical and arithmetic operations. In this article, we will look into different types of Python operators. 
- Arithmetic operators are used to performing mathematical operations like addition, subtraction, multiplication, and division:
- Example: 
```
# Examples of Arithmetic Operator
a = 9
b = 4
 
# Addition of numbers
add = a + b
 
# Subtraction of numbers
sub = a - b
 
# Multiplication of number
mul = a * b
 
# Division(float) of number
div1 = a / b
 
# Division(floor) of number
div2 = a // b
 
# Modulo of both number
mod = a % b
 
# Power
p = a ** b
 
# print results
print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)
print(p)
```
- Comparison Operators: Comparison of Relational operators compares the values. It either returns True or False according to the condition.
- Example: 
```
# a > b is False
print(a > b)
 
# a < b is True
print(a < b)
 
# a == b is False
print(a == b)
 
# a != b is True
print(a != b)
 
# a >= b is False
print(a >= b)
 
# a <= b is True
print(a <= b)
```
- Logical operators perform Logical AND, Logical OR, and Logical NOT operations. It is used to combine conditional statements.
- Example: 
```
# Examples of Logical Operator
a = True
b = False
 
# Print a and b is False
print(a and b)
 
# Print a or b is True
print(a or b)
 
# Print not a is False
print(not a)
```
- Bitwise Operators: Bitwise operators act on bits and perform the bit-by-bit operations. These are used to operate on binary numbers.
- Example:
```
# Print bitwise AND operation
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation
print(~a)

# print bitwise XOR operation
print(a ^ b)

# print bitwise right shift operation
print(a >> 2)

# print bitwise left shift operation
print(a << 2)
```
- Assignment Operators 
- Example
```
# Examples of Assignment Operators
# Assign value
b = a
print(b)

# Add and assign value
b += a
print(b)

# Subtract and assign value
b -= a
print(b)

# multiply and assign
b *= a
print(b)

# bitwise lishift operator
b <<= a
print(b)
```
- Identity Operators: is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 
- Example:
```
a = 10
b = 20
c = a

print(a is not b)
print(a is c)
```
- Membership Operators: in and not in are the membership operators; used to test whether a value or variable is in a sequence
```
# Python program to illustrate
# not 'in' operator
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
	print("x is NOT present in given list")
else:
	print("x is present in given list")

if (y in list):
	print("y is present in given list")
else:
	print("y is NOT present in given list")
```


