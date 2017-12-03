given= input("input binary number")
def convertToDecimal (startNum):
    powOf2 = len(startNum)-1
    addition=0
    for ch in startNum:
        power=2**powOf2
        #print(power)
        multiplied= int(ch)*power
        addition = addition + multiplied
        powOf2=powOf2 - 1
    return addition
print(convertToDecimal(given))
