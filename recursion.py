LL: Merge Two Sorted Linked Lists -----
def MergeLists(list1, list2):
    if (list1 == None):
        return list2
    if (list2 == None):
        return list1

    if (list1.data < list2.data):
        list1.next = MergeLists(list1.next, list2)
        return list1
    else:
        list2.next = MergeLists(list2.next, list1)
        return list2

Binary Search -------------
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
			return -1