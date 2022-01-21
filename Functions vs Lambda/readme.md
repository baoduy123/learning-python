### Functions vs Lambda
- Python Lambda Functions are anonymous function means that the function is without a name. As we already know that the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python
- Python Lambda Function Syntax:
```
lambda arguments: expression
```
	- This function can have any number of arguments but only one expression, which is evaluated and returned.
	- One is free to use lambda functions wherever function objects are required.
	- You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.	
	- It has various uses in particular fields of programming besides other types of expressions in functions.
- Example:
```
# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
	return y*y*y

lambda_cube = lambda y: y*y*y

# using the normally
# defined function
print(cube(5))

# using the lambda function
print(lambda_cube(5))
```
