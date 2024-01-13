def cipherMain(initial, final, msg):
    ceasar = initialize(initial, final)
    message = encoded(ceasar,msg)
    print(message)
    
def initialize(initial, final):    
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    alphaMap = createAlphaMap(alphabet)
    #initial = input('choose starting letter: ').lower()
    #final = input('choose letter you want to shift to: ').lower()
    ceasar = createCeasarMap(alphabet, initial, final, alphaMap)
    return ceasar

def encoded(ceasar,msg):
    message = msg #input("Choose a message to encode: ")
    encoded = ''
    for ch in message:
        upper = False
        if ch.isupper():
            upper = True
        if ch.lower() in ceasar:
            if upper:
                encoded += (ceasar[ch.lower()]).upper()
            else:
                encoded += ceasar[ch]
        else:
            encoded += ch
    return encoded

def createAlphaMap(alphabet):
    alphabetMap = {}
    for i in range(len(alphabet)):
        alphabetMap[alphabet[i]] = i + 1
    return alphabetMap

def createCeasarMap(alphabet, initial, final, alphaMap): #initial is the starting point, final is the desired number.
    shiftMap = createAlphaMap(alphabet)
    shifts = shift(shiftMap, initial, final, alphaMap)
    ceasar = {}
    swapShift = dict((index,letter) for (letter, index) in shifts.items())
    for letter in alphaMap:
        ceasar[letter] = swapShift[alphaMap[letter]]
    return ceasar

def shift(shiftMap, initial, final, alphaMap):
    intIndex = alphaMap[initial]
    finIndex = alphaMap[final]
    change = finIndex - intIndex
    for i in shiftMap:
        shiftMap[i] += change
        if shiftMap[i] > 26:
            shiftMap[i] -= 26
        elif shiftMap[i] < 1:
            shiftMap[i] += 1
    return shiftMap
