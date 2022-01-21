**Module**
  - In Python, Modules are simply files with the “.py” extension containing Python code that can be imported inside another Python Program. In simple terms, we can consider a module to be the same as a code library or a file that contains a set of functions that you want to include in your application.

  - With the help of modules, we can organize related functions, classes, or any code block in the same file. So, It is considered a best practice while writing bigger codes for production-level projects in Data Science is to split the large Python code blocks into modules containing up to 300–400 lines of code.

  - The module contains the following components:
    - Definitions and implementation of classes,
    - Variables, and
    - Functions that can be used inside another program.
  - Example:
    In this program, a function is created with the name “welcome” and save this file with the name mymodule.py i.e. name of the file, and with the extension “.py”. Save the following code in a file named mymodule.py
  ```
  def welcome(name):
    print("Hello, " + name +", welcome to TMA")
  ``` 
  In this example, we will Import the module named mymodule, and then call the welcome function with a given argument:
  ```
  import mymodule
  mymodule.welcome("Bao Duy")
  ```
  **Packages**
  - Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module; definitions from a module can be imported into other modules or into the main module (the collection of variables that you have access to in a script executed at the top level and in calculator mode). A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__.
  - Example:  Fibonacci numbers module
```
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```
```
import fibo
fibo.fib(1000)
fibo.fib2(100)
```
