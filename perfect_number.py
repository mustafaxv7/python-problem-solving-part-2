# A programm to tell if a number is perfect or not
def isPerfect(number):
    somme_div = 0
    for i in range(1,int(number//2)+1):
        if number % i == 0 :
            somme_div+=i
    if number == somme_div :
        return True
    else: return False

number = int(input("\nEnter a Number>>: "))
# print(isPerfect(number))
if isPerfect(number):
    print(f"\n{number} is Perfect\n")
else: print(f"\n{number} is Not Perfect\n")