
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
#Given a 2d Array of size N^2, calculate the difference between a 
#Diagonal line from Top Left to Bottom Right, vs. Top Right to Bottom Left
def forwardSlash(arr):
    ans = 0             #Finds the sum of Top Left to Bottom Right
    for i in range(len(arr)):
        ans += arr[i][i]
    return ans

def backSlash(arr): 
    ans = 0
    width = len(arr)
    for i in range(width): #Finds the sum of Top Right to Bottom Left
        j = width -1 - i
        ans += arr[i][j]
    return ans

def diagonalDifference(arr):
    leftDiag = forwardSlash(arr)
    rightDiag = backSlash(arr)
    return abs(leftDiag-rightDiag) #Returns absolute value of the difference

# Given an Array, print the ratio of positive integers to total length
# Do the same for Negative and Zeroes
def plusMinus(arr):
    posScore=0
    negScore = 0
    zeroScore = 0
    denom = len(arr)
    for i in arr:
        if i >0:
            posScore +=1
        elif i < 0:
            negScore +=1
        else:
            zeroScore +=1
    print(float(posScore/denom))
    print(float(negScore/denom))
    print(float(zeroScore/denom))



#Given an integer, print a staircase of height N, where the top step consist of
# one '#', preceded by all ' ', and the bottom step contains all '#'
def staircase(n):
    ansArray=[]
    for i in range(n):
        j = n-i
        for num in range(n):
            if num>=j-1:
                ansArray.append("#")
            else:
                ansArray.append(" ")
        print(str(''.join(ansArray)))
        ansArray = []

# Complete the birthdayCakeCandles function below.
#Given an array, how many 'candles' (integers) are of the tallest height?
def birthdayCakeCandles(ar):
    tallestCandle = 0
    numberOfTalls = 0
    for i in ar:
        if i == tallestCandle:
            numberOfTalls += 1
        if i > tallestCandle:
            tallestCandle = i
            numberOfTalls =1
    return numberOfTalls


#Given a time in format "HH:MM:SS AM/PM", convert it to 24hr time,
#in the format HH:MM:SS
def timeConversion(s):
    original = s.split(":")
    original[0]= str(int(original[0])%12)
    if "P" in s:
        original[0] = str((int(original[0])+12)%24)
    else:
        original[0]=original[0].zfill(2)
    converted = ":".join(original)
    converted = converted[:8]
    return converted

