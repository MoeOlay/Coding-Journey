def RGB_to_CMYK(Red , Green, Blue):
    RGB = {}
    CMYK = {}
    RGB['Red'] = Red
    RGB['Green'] = Green
    RGB['Blue'] = Blue
    RPrime = Red/255
    GPrime = Green/255
    BPrime = Blue/255
    KPrime = 1 - max(RPrime, GPrime, BPrime)
    CMYK['C'] = int((1-RPrime - KPrime)*100/(1-KPrime))
    CMYK['M'] = int((1-GPrime - KPrime)*100/(1-KPrime))
    CMYK['Y'] = int((1-BPrime - KPrime)*100/(1-KPrime))
    CMYK['K'] = round((KPrime * 100))
    print(f'\nCMYK Values\nCyan: {CMYK['C']}\nMagenta: {CMYK['M']}\nYellow: {CMYK['Y']}\nKey (Black): {CMYK['K']}')
while True:
    print("RGB To CMYK Converter")
    R = input("Enter the Red Color Value: ")
    if R == 'q' or R == 'quit':
        break
    G = input("Enter the Green Color Value: ")
    if G == 'q' or G == 'quit':
        break
    B = input("Enter the Blue Color Value: ")
    if B == 'q' or B == 'quit':
        break
    R = int(R)
    G = int(G)
    B = int(B)
    RGB_to_CMYK(R,G,B)


