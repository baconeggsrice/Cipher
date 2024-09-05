def cipherMain(info):
    initial, final, msg = info[1], info[2], info[3]
    ceasar = initialize(initial, final)
    message = encoded(ceasar,msg)
    return message

def decoding(decodeInfo):
    initial, final, msg = decodeInfo[1], decodeInfo[2], decodeInfo[2]
    ceasar = initialize(initial, final)
    decodedMsg = decode(ceasar, msg)
    return decodedMsg
    
def initialize(initial, final):    
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    alphaMap = createAlphaMap(alphabet)
    ceasar = createCeasarMap(alphabet, initial, final, alphaMap)
    return ceasar

def encoded(ceasar,msg):
    encoded = ''
    for ch in msg:
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

def decode(ceasar, msg):
    decoded = ''
    ceasarKey = dict((index, letter) for (letter, index) in ceasar.items())
    for ch in msg:
        upper = False
        if ch.isupper():
            upper = True
        if ch.lower() in ceasarKey:
            if upper:
                decoded += (ceasarKey[ch.lower()]).upper()
            else:
                decoded += ceasarKey[ch]
        else:
            decoded += ch
    return decoded

def createAlphaMap(alphabet):
    alphabetMap = {}
    for i in range(len(alphabet)):
        alphabetMap[alphabet[i]] = i + 1
    return alphabetMap

def createCeasarMap(alphabet, initial, final, alphaMap): #initial is the starting point, final is the desired number.
    if initial == final:
        return alphaMap
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
            shiftMap[i] += 26
    return shiftMap