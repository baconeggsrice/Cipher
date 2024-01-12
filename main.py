def main():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    alphaMap = alphaMap(alphabet)

def alphaMap(alphabet):
    alphabetMap = dict(enumerate(alphabet,1))
    return alphabetMap

if __name__ == "__main__":
    main()