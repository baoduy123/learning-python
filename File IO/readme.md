  - Python's built-in functions input() and print() perform read/write operations with standard IO streams. The input() function reads text into memory variables from keyboard which is defined as sys.stdin and the print() function send data to display device identified as sys.stdout. The sys module presents definitions of these objects. 
  - Instead of standard output device, if data is saved in persistent computer files then it can be used subsequently. File is a named location in computer’s non-volatile storage device such as disk. Python's built-in function open() returns file object mapped to a file on the permanent storage like disk.
 ```
    import os
    #Open a file
    fo=open('text.txt','w')

    # The file Object Attributes
    print('\nThe file Object Attributes:')
    print(f"Name of the file:{fo.name}")
    print(f"Closed or not:{fo.closed}")
    print(f"Opening mode:{fo.mode}")

    #Write a file
    fo.write("Hello World")

    #Close a file
    fo.close()

    #Read a file
    fo=open('text.txt','r') 
    t_9=fo.read(10)
    #Reposition pointer at the beginning of the file because the current pointer's position is 10
    fo.seek(0,0)
    print(f'\nRead 10 first character of file: {t_9}')
    t_full=fo.read()
    print(f'\nContent of file: {t_full}')
    fo.close()

    #Renaming a file 
    os.rename('text.txt','final_text.txt')
    print("\nChanged name of file from text.txt to final_text.txt")

    #Remove a file
    os.remove('final_text.txt')
    print("\nfile final_text.txt has been removed")
```
