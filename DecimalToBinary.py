# program to convert a decimal number to binary
def decimalTobinary(number):
    binary_number = 0
    order = 0
    while (number != 0):
        rest = number % 2
        p = 10 ** order
        binary_number = binary_number + (rest * p)
        order +=1
        number = number // 2
    return binary_number
decimal_number = int(input("\n\nEnter a Decimal Number>>: "))
print(f" \n\n{decimal_number} in binary is : {decimalTobinary(decimal_number)}\n\n")


