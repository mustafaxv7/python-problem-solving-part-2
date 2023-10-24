# This programm to find the PGCD of two numbers

def PGCD( num1 , num2):
    while True:
        rest = num1 % num2
        num1 =  num2
        num2 = rest
        if rest == 0:
            break
    return num1
# Another solution two find PGCD 
def PGCD_2(num1 , num2):
    if num1 < num2:
        min = num1
    else: min = num2
    for i in range(1,min+1):
        if (num1 % i == 0 and num2 % i == 0):
            pgcd = i
    return pgcd

numberOne = int(input("\nEnter The First Number>>: \n"))
numberTwo = int(input("\nEnter The Second Number>>: \n"))
print(f"\nThe PGCD of These two numbers is: {PGCD(numberOne,numberTwo)}\n")
# print(f"\nThe PGCD of These two numbers is: {PGCD_2(numberOne,numberTwo)}\n")