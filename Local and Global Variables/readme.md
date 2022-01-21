- Global variables are those which are not defined inside any function and have a global scope whereas local variables are those which are defined inside a function and its scope is limited to that function only. In other words, we can say that local variables are accessible only inside the function in which it was initialized whereas the global variables are accessible throughout the program and inside every function. 
- Local variables are those which are initialized inside a function and belongs only to that particular function. It cannot be accessed anywhere outside the function.
  - Example:
```
#Local variable
 def f():

	# local variable
	s = "I am Bao Duy"
	print(s)

# Driver code
f()
Result: I am Bao Duy
```
```
# This function uses global variable s
def f():
	s = " I am Duy" 
	print(s)

# Global scope
s = "I am Bao Duy"
f()
print(s)
Result: 
I am Duy
I am Bao Duy
```
