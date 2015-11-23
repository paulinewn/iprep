SEARCH UNSORTED ARRAY ----------------------------------------------------------------------------------------

def search(value, size, array):
    count=0
    for i in array[0:size]:
        val = int(i)
        if (val == value):
            print count
        val+=1
        count+=1
    return count
value = int(raw_input())
size = int(raw_input())
array = raw_input().split()
search (value,size,array)

Insertion Sort  --------------------------------------------------------------------------------
def insertionSort(ar): 
    for i in range(0,len(ar)):
        currentVal = ar[i]
        print ar[i]
        pos=i
        j = i -1
        while j >= 0 and ar[j] > currentVal:
            ar[j+1] = ar[j]
            j=j-1 
            ar [j+1]=currentVal
            print ar

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

Insertion Sort: Strings ------------------------------------------------------
def insertionSort(ar): 
    for i in range(0,len(ar)):
        currentVal = ar[i]
        pos=i
        j = i -1
        while j >= 0 and ar[j] > currentVal:
            ar[j+1] = ar[j]
            j=j-1 
            stringconv(ar)
        ar [j+1]=currentVal
    stringconv (ar)
    
def stringconv(ar):
    string=""
    for i in ar:
        char = str(i)
        string+= char+" "
    print string
        
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

QUICKSORT ---------------------------------------------------------------------------
#!/bin/python
def partition(ar):    
    less = []
    equal = []
    greater = []
    if len(ar) <=1:
        return ar
    else:
        pivot = ar[0]
        for x in ar:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
    return partition(less) + equal + partition(greater)
    
def stringconv(ar):
    string=""
    for i in ar:
        char = str(i)
        string+= char+" "
    print string

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
stringconv( partition(ar))

QUICKSORT -------------------------------------------------------------
#!/bin/python
def quicksort(ar):    
    less = []
    equal = []
    greater = []
    if len(ar) <=1:
        return ar
    else:
        pivot = ar[0]
        for x in ar:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        quicksort(less)
        quicksort(greater)
    stringconv(less + equal + greater)
def stringconv(ar):
    string=""
    for i in ar:
        char = str(i)
        string+= char+" "
    print string

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quicksort(ar)

------------------------
quicksort(A, lo, hi)
  if lo < hi
    p = partition(A, lo, hi)
    quicksort(A, lo, p)
    quicksort(A, p + 1, hi)

partition(A, lo, hi)
    pivot = A[lo]
    i = lo - 1
    j = hi + 1
    while True
        do
            j = j - 1
        while A[j] > pivot
        do
            i = i + 1
        while A[i] < pivot
        if i < j
            swap A[i] with A[j]
        else 
            return j

COUNTING SORT -----------------------------------
def counting_sort(array, maxval):
    """in-place counting sort"""
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return (array,count)
COUNTING SORT HACKERRANK -----------------------------------
def counting_sort(array):
    max=0
    for elem in array:
        if elem > max:
            max= elem
    size = max + 1
    count = [0] * size
    for a in array:
        count[a] += 1
    i=0
    for a in range(m):
        for c in range(count[a]):
            array[i]=a
            i+=1
    return count

def stringconv(A):
    string =""
    for i in A:
        char = str(i)
        string += char+" "
    print string
    
m=input()
a= [int(i) for i in raw_input().strip().split()]
stringconv(counting_sort(a))

______
# Enter your code here. Read input from STDIN. Print output to STDOUT
def nohumor(a):
    for case in a[-1]:
        s = input()
        rs = s[::-1]
        n= len(s)
        for i in range (1, n):
            d1 = abs(ord(s[i]) - ord(s[i-1]))
            d2 = abs (ord(rs[i]) - ord(rs[i-1]))
            if d1 != d2:
                print("Not Funny")
                break
            else:
                print("Funny")
    
def stringconv(A):
    string =""
    for i in A:
        char = str(i)
        string += char+" "
    print string
    
m=input()
a= raw_input()
nohumor(a)