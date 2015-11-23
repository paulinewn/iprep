Arrays: 2D Hourglass -------------------------------------------------

#2D Array Hourglass
# Enter your code here. Read input from STDIN. Print output to STDOUT
arrayList = [raw_input().split() for x in range(0, 6)]
intMatrix = [list(map(int, x)) for x in [list(x) for x in arrayList]]

def checkCoordinate(matrix, x, y):
    '''given a coordinate of the matrix 2d plane, calculates the sum
    of the hourglass starting with the top left of the hourglass being
    the coordinates given'''
    hourTop = matrix[y][x:x+3]
    hourBottom = matrix[y+2][x:x+3]
    hourMiddle = matrix[y+1][x+1]
    hourglass = sum(hourTop) + hourMiddle + sum(hourBottom)
    return hourglass

def loopCoords(matrix):
    '''loops through all coordinates that can make a full hourglass.
    returns the greatest hourglass sum'''
    greatest = checkCoordinate(matrix, 0, 0)
    current = 0
    for i in range(4):
        for z in range(4):
            current = checkCoordinate(matrix, z, i)
            if current > greatest:
                greatest = current
            else: pass
    return greatest

print(loopCoords(intMatrix))


Intersection no hashmap: Find two intersections of an array ----------------------------------------------------------
def intersection (arr1, arr2):
    i=0
    j = 0
    m = len(arr1)//len(arr2)
    n= len(arr2)//len(arr1)
    while (i< m and j < n):
        if arr1[i] < arr2[j]:
            i+=1
        elif arr2[j]<arr1[i]:
            j+=1
        else:
            i+=1
            print " %d ", arr2[::1]
            i+=1
O( len(arr1 + len(arr2))

Intersection: Find intersections of two unsorted arrays ------------------------------------------
def intersectUnsorted (arr1, arr2):
    i=0
    m= len(arr1)
    n= len(arr2)
    #make sure one array is smaller, if it isnt make arr1 the smaller array 
    if len(arr1) > len (arr2):
        arr1, arr2= arr2, arr1
        #swap
        m, n = n, m
        arr1.sort()
        for i in range(n):
            if (bs (arr1, arr2[i])):
                print arr2[i]

Union: Find union of two unsorted arrays ----------------------------------------------
def unionUnsorted (arr1, arr2):
    i=0
    m= len(arr1)
    n= len(arr2)
    #make sure one array is smaller, if it isnt make arr1 the smaller array 
    if len(arr1) > len (arr2):
        arr1, arr2= arr2, arr1
        #swap
        m, n = n, m
        arr1.sort()
        for i in range(m):
            print arr1[i]
        for i in range(n):
            if (bs (arr1, arr2[i])==False):
                print arr2[i]
