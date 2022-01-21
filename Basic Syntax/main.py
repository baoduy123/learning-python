# define main function to print out something
import keyword


def main():
    i = 1
    a,b,c = 1, 2, 3
    max = 10
    while (i < max):
        print(i)
        i = i + 1
    if (a == 1) and (b == 3) and \
      (c == 2 ):
        print("Continuation of statements")
    s = 'This is a string'
    print(s) 
    s = "Another string using double quotes"
    print(s)
    s = ''' string can span
        multiple line '''
    print(s)
# call function main 
if __name__=='__main__':
    main()
