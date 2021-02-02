def leap(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                print(n, 'is a leap year')
                return
            print(n, 'is not a leap year')
            return
        print(n, 'is a leap year')
        return
    print(n, 'is not a leap year')
    return

import time
print("This program will determine whether a year you enter is a leap year or not")
while True: 
    try:
        value = int(input("Enter in a year number: "))
        leap(value)
        time.sleep(5)
        break
    except ValueError:
        print("Whoops! you put in something you weren't supposed to.")
    
    
            
