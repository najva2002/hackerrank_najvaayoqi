#Solve me first

def solveMeFirst(a,b):
    return a+b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)

#simple Array sum 

import os

def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result))
    fptr.close()

#compare the Triplets
import os

def compareTriplets(a, b):
    result = [0,0]

    for i in range(len(a)):
        if a[i] > b[i]:
            result[0] += 1
        elif a[i] < b[i]:
            result[1] += 1

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.close()

#A Very Big Sum
import os

def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result))
    fptr.close()

















#Diagonal Difference
import os

def diagonalDifference(arr):
    left = 0
    right = 0
    for i in range(len(arr)):
        left += arr[i][i]
        right += arr[i][len(arr)-1-i]

    return abs(left-right)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result))
    fptr.close()













#plus MINUS
def plusMinus(arr):
    p = 0
    n = 0
    z = 0
    l = len(arr)

    for i in arr:
        if i == 0:
            z += 1
        elif i < 0:
            n += 1
        else:
            p += 1
    print(p/l)
    print(n/l)
    print(z/l)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

staircase
def staircase(n):
    for i in range(n):
        r = ""
        for j in range(n-1-i):
            r += " "
        for j in range(i+1):
            r += "#"
        print(r)

if __name__ == '__main__':
    n = int(input())

    staircase(n)



#Mini-Max Sum
def miniMaxSum(arr):
    arr.sort()

    print(sum(arr[:4]), sum(arr[-4:]))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
#Birthday cake candles
import os

def birthdayCakeCandles(ar):
    return ar.count(max(ar))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result))
    fptr.close()

#Time conversion
import os

def timeConversion(s):
    a = int(s[:2])

    if "PM" in s:
        if a != 12:
            a += 12
        a = str(a)
    else:
        if a == 12:
            a = '00'
        else:
            a = '0' + str(a)

    return a + s[2:8]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result)
    f.close()

#BIG sorting
import os

def bigSorting(unsorted):
    return sorted(unsorted, key = int)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.close()




#INTRO to tutorial ch allenges

import os

def introTutorial(V, arr):
    return arr.index(V)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input())
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result))
    fptr.close()

#Insertion sort- part1
def insertionSort1(n, arr):
    tmp = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] > tmp:
            arr[i+1] = arr[i]
            print(' '.join(map(str, arr)))
        else:
            arr[i+1] = tmp
            print(' '.join(map(str, arr)))
            return

    arr[0] = tmp
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#Insertion sort –part2
def insertionSort2(n, arr):
    for i in range(1, n):
        tmp = arr[i]
        j = i-1

        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = tmp

        print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

#correctness and the loop invariant

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))




#Quicksort 1- partition
import os

def quickSort(arr):
    pivot = arr[0]
    left, right = [], []

    for i in arr[1:]:
        if i <pivot:
            left.append(i)
        else:
            right.append(i)

    return left + [pivot] + right

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.close()

#counting sort 1
import os

def countingSort(arr):
    ret = [0 for _ in range(100)]

    for i in arr:
        ret[i] += 1
    return ret
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.close()

#counting sort 2
import os

def countingSort(arr):
    s = [0 for _ in range(100)]
    ret = []

    for i in arr:
        s[i] += 1

    for i in range(len(s)):
        for j in range(s[i]):
            ret.append(i)

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.close()

#closest Numbers
import os
import sys

def closestNumbers(arr):
    minDif = sys.maxsize
    ret = []
    arr.sort()
  
    for i in range(len(arr)-1):
        dif = abs(arr[i] - arr[i+1])
        if dif < minDif:
            minDif = dif
            ret = [arr[i], arr[i+1]]
        elif dif == minDif:
            ret.append(arr[i])
            ret.append(arr[i+1])

    return ret
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.close()

#Running Time of algorithms
import os

def runningTime(arr):
    ret = 0
    for i in range(1, n):
        tmp = arr[i]
        j = i-1

        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j -= 1
            ret += 1

        arr[j+1] = tmp

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result))
    fptr.close()

#super Reduced string
import os

def superReducedString(s):
    reducedString = []

    for i in s:
        if len(reducedString) == 0 or i != reducedString[-1]:
            reducedString.append(i)
        else:
            reducedString.pop()

    if len(reducedString) == 0:
        return "Empty String"

    return ''.join(reducedString)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result)
    fptr.close()

#camelcase
import os
def camelcase(s):
    ret = 1

    for i in s:
        if 'A' <= i <= 'Z':
            ret += 1
    return ret
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = camelcase(s)
    fptr.write(str(result))
    fptr.close()

#strong password
import os

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    requiredNumber = 1
    requiredLower = 1
    requiredUpper = 1
    requiredSpecial = 1

    for i in password:
        if i in numbers:
            requiredNumber = 0
        elif i in lower_case:
            requiredLower = 0
        elif i in upper_case:
            requiredUpper = 0
        elif i in special_characters:
            requiredSpecial = 0

    ret = requiredNumber + requiredLower + requiredUpper + requiredSpecial

    if len(password) + ret < 6:
        return 6 - len(password)

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer))
    fptr.close()


#TWO Characters
import os
from itertools import combinations

def alternate(s):
    st = list(set(s))

    if len(st) < 2:
        return 0

    combination = list(combinations(st, len(st)-2))

    ret = 0
    for com in combination:
        tmp = s

        for i in com:
            tmp = tmp.replace(i, "")

        canMake = True

        for i in range(len(tmp)-1):
            if tmp[i] == tmp[i+1]:
                canMake = False
                break

        if canMake and len(tmp) > ret:
            ret = len(tmp)

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())
    s = input()

    result = alternate(s)

    fptr.write(str(result))
    fptr.close()
#Caesar cipher
import os

def shiftAlphabet(c, k):
    if 65 <= c <= 90:
        c += k
        if c < 65:
            c += 26
        elif c > 90:
            c -= 26
    elif 97 <= c <= 122:
        c += k
        if c < 97:
            c += 26
        elif c > 122:
            c -= 26

    return chr(c)

def caesarCipher(s, k):
    ret = []
    k %= 26
    for i in s:
        ret.append(shiftAlphabet(ord(i), k))

    return ''.join(ret)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    s = input()
    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result)
    fptr.close()

