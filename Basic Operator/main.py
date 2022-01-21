def main():
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
  # Print a and b is False
  print(a and b)
  
  # Print a or b is True
  print(a or b)
  
  # Print not a is False
  print(not a)
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

if __name__ == '__main__':

    main()

