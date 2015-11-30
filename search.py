Search: Unsorted Array ----------------------------------------------------------------------------------------

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

Binary Search: Unsorted Array ------------------------------------------------------------
def bs (arr, x):
	if len(arr) == 0:
		return False
	else:
		midpoint = len(arr)//2
		if arr[midpoint] == x:
			return True
		else:
			if x< arr[midpoint]:
				return bs ( arr[:midpoint],x)
			else:
				return bs (arr[midpoint+1:],x)

Binary Search: BT Tree ------------------------------------------------------------
def bs (arr, x):
	if len(arr) == 0:
		return False
	else:
		midpoint = len(arr)//2
		if arr[midpoint] == x:
			return True
		else:
			if x< arr[midpoint]:
				return bs ( arr[:midpoint],x)
			else:
				return bs (arr[midpoint+1:],x)

Order Statistics ---------------------
# Enter your code here. Read input from STDIN. Print output to STDOUT
def orderstats (array, k):
    greater = []
    less= []
    equal = []
    pivot = array[0]
    for i in array:
        if i < pivot:
            less.append(i)
        if i > pivot:
            greater.append(i)
        if i == pivot:
            equal.append(i)
    if len(greater) >= k:
        return orderstats(greater, k)
    if len(greater) == k-1:
        return pivot
    if len(greater) < k:
        return orderstats (less, k-len(equal) -len(greater))
    

m = input()
size = m//2+1
ar = [int(i) for i in raw_input().strip().split()]
print orderstats(ar, size)