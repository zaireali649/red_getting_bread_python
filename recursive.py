def summation(x):
    try:
        x = int(x)
    except:
        return 0

    if(x == 1):
        return 1
    else:
        return x + summation(x-1)

if(__name__ == '__main__'):
    print(1 + 2)
    print(1 + 2 + 3)
    print(1 + 2 + 3 + 4)

    print(summation(2)) # 3
    print(summation(3)) # 6
    print(summation(4)) # 10
    print(summation(55)) # 1540