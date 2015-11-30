ARRAYS

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