num1 = int(input('Enter your number: '))

def collatz(num1):
    while num1 != 1:
        print(num1, '->', end=' ')
        if num1 % 2 == 0:
            num1 = num1 // 2
        else:
            num1 = num1 * 3 + 1
    print(1)  
    return num1

collatz(num1)
