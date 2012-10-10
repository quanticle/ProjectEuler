#! /usr/bin/python
ones = [ "",
         "one",
         "two", 
         "three", 
         "four", 
         "five", 
         "six", 
         "seven", 
         "eight",
         "nine", 
         "ten", 
         "eleven",
         "twelve",
         "thirteen",
         "fourteen",
         "fifteen",
         "sixteen",
         "seventeen",
         "eighteen",
         "nineteen" ]

tens = [ "",
         "",
         "twenty",
         "thirty", 
         "forty",
         "fifty",
         "sixty",
         "seventy",
         "eighty",
         "ninety"]

def sayNumber(number):
    spokenNumber = ""
    numHundreds = number / 100
    if numHundreds > 0:
        spokenNumber += "%s hundred " % ones[numHundreds]
    number = number % 100
    if number > 0 and numHundreds > 0:
        spokenNumber += "and "
    numTens = number / 10
    if numTens > 1:
        spokenNumber += "%s " % tens[numTens]
        number = number % 10
        spokenNumber += "%s" % ones[number]
    else:
        number = number % 20
        spokenNumber += "%s" % ones[number]


    return spokenNumber

def main():
    outputFile = open("output.txt", 'w')
    for i in xrange(999, 0, -1):
        print >>outputFile, sayNumber(i)

if __name__ == '__main__':
    main()
