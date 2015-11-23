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