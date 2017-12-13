#convert int to string
def convertIntToSym(value):
    if value in range (0,10):
        sym = chr(value +48)
    else:
        sym = chr(value +55)
    return sym
    
#convert sym to decimal value
def convertSym(sym):
    ordVal = ord(sym)
    if ordVal in range(48,58):
        result = ordVal - 48
    else:
        result = ordVal - 55
    return result

def convertToDecimal (startNum, startBase):
    powOfX = len(startNum)-1
    addition=0
    for ch in startNum:
        power=startBase**powOfX
        #print(power)
        multiplied= convertSym(ch)*power
        addition = addition + multiplied
        powOfX = powOfX - 1
    return addition
def test():
    print(convertSym('0') == 0)
    print(convertSym('1') == 1)
    print(convertSym('A') == 10)
    print(convertSym('Z') == 35)
    print(convertIntToSym(0) == '0')
    print(convertIntToSym(10) == 'A')
def main():
    given= input("input binary number")
    print(convertToDecimal(given, 16))
#test()
main()
