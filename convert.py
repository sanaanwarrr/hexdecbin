convert = int(input("type 1 to convert from decimal to hexadecimal or 2 to convert from hexadecimal to decimal: "))
conversionKey = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

# input: ask for decimals, hexadecimals, binary
# output: ask for decimals, hexadecimals, binary

if (convert == 1): # decimal to hexadecimal
    hexResult = ''
    dec = int(input("enter decimal number: "))
    if (dec == 0):
        hexResult = '0'
    else:
        while (dec > 0):
            remainder = dec % 16
            hexResult = conversionKey[remainder] + hexResult
            dec = dec // 16
    print("hexadecimal number: " + hexResult)

elif (convert == 2):
    hex = input("enter hexadecimal number: ")
    decResult = 0
    hexLength = len(hex)
    for char in hex:
        digit = conversionKey.index(char.upper())
        decResult += digit * (16 ** (hexLength-1))
        hexLength -= 1
    
    print("decimal number: " + str(decResult))
    
else:
    print("invalid input")

