import random

number = random.randint(0,3)
print(number)

try:
    print(1/number)
    print(1/"d")
except ZeroDivisionError:
    print("ZeroDivisionError")
    print(0)
except Exception as e: # general error
    print(e)    
    pass

print("Done")