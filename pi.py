import math
import time

with open("./100000.txt") as piFile:
    piContent = piFile.read()[2:]


def isPrime(num: int) -> bool:
    numAsString = str(num)
    numSum = 0

    if int(numAsString[-1]) in [0, 5]:
        return False

    if num % 2 == 0:
        return False

    for char in numAsString:
        numSum += int(char)

    if numSum % 3 == 0:
        return False

    for i in range(7,  math.ceil(math.sqrt(num))):
        if (num % i) == 0:
            return False

    return True


def findNthPrime(nMax: int, width: int = 15):
    nthPrime = 0
    pos = 0
    while True:

        num = int(piContent[pos:(pos+width)])
        pos += 1

        if isPrime(num):
            nthPrime += 1
            print(f"Prime nr. {nthPrime} found: {num}, Position: {pos}")

            if nthPrime == nMax:
                break

n = 1
length = 10
t0 = time.time()
findNthPrime(n, length)
t1 = time.time()

print(f"Time to find {n}th element:{t1-t0}s")

