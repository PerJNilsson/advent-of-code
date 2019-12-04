def extractIntegers(number):
    integers = []
    while number > 1:
        integers.append(int(number % 10))
        number = number / 10
    return integers[::-1]

def countPasswords(min, max):
    numPasswords = 0
    for num in range(min, max+1):
        ints = extractIntegers(num)
        if (checkSameAdjecentDigits(ints) and checkAscendingOrder(ints)):
            numPasswords += 1
    return numPasswords
            
        
def checkSameAdjecentDigits(ints):
    for i in range(0, len(ints)-1):
        if (ints[i] == ints[i+1]):
            return True
    return False

def checkAscendingOrder(ints):
    if (ints[0] <= ints[1] <=ints[2] <=ints[3] <= ints[4] <= ints[5]):
        return True
    return False

def main():
    min = 108457
    max = 562041

    numPasswords = countPasswords(min,max)

    print(numPasswords)
if __name__ == '__main__':
    main()
