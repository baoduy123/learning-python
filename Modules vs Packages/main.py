import modules as md
import Package as pg
def main():
   md.welcome("Bao Duy")
   print("Write Fibonacci series up to 100")
   pg.fib.fib(100)
   print("Fibonacci series up to 1000")
   result = pg.fib2.fib2(1000)
   print(result)

if __name__ == '__main__':

    main()
   
  
