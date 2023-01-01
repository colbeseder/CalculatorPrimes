import sys

letterLookup = "OIZEHSGLBB"

numLookup = {}
for i, c in enumerate(letterLookup[0:-1]):
    numLookup[c] = str(i)

words = []

def readInWordList(wordListPath):
    global words
    with open(wordListPath) as f:
        words = set([line.rstrip() for line in list(f)])

def num2word(n):
    s = str(n)
    r = [letterLookup[int(x)] for x in s]
    r.reverse()
    return ''.join(r)

def word2num(w):
    try:
        n = [numLookup[x] for x in reversed(w)]
    except:
        return False
    return ''.join(n)

def isWordable(n):
    w = num2word(n)
    return w in words

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

def isPrimable(s):
    n = word2num(s)
    if n and isPrime(int(n)):
        return True
    return False

def checkPrimes():
    with open("resources/primes.txt") as file:
        for line in reversed(list(file)):
            n = line.rstrip()
            if isWordable(n):
                print("%s : %s"%(num2word(n), n))

def checkWords():
    results = []
    for w in words:
        if isPrimable(w):
            results.append((w, int(word2num(w))))
    return results

if __name__ == "__main__":
    wordListPath = sys.argv[1]
    readInWordList(wordListPath)
    results = sorted(checkWords(), key=lambda x: x[1], reverse=True)
    for result in results:
        print("%-12s   %s"%(result[1], result[0]))
    