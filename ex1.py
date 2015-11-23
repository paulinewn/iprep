import time 
def timer1():
	start_time = time.clock()
	allPermutations("seth",0)
	print time.clock() - start_time, "seconds"
def timer2():
	start_time = time.clock()
	listCompPermute("seth")
	print time.clock() - start_time, "seconds"

def allPermutations (string, step=0):
	#print permutation if end reached
	if step == len(string):
		print "".join(string)
	for i in range(step, len(string)):
		#copy string and store as an array
		stringc = [char for char in string]
		#swap current index with step
		stringc[step], stringc[i]= stringc[i], stringc[step]
		#recurse on unswapped portion of string
		allPermutations (stringc, step+1)
def listCompPermute (num):
	## len(num) < 1 , return [[]]
	## insert each new value into possible interspaces
	##which there are n+1 of them  if there are n chars already 
	results =[[]]
	for x in num:
		results = [r[:i] +[x] + r[i:] for r in results for i in range (len(r)+1)]
	return results
def replace(string, pos, new):
    lengthNew = len(new)
    if pos >= len(string):
    	return "too large"
    if pos <= 0:
    	return "Impossible" 
    for char in string:
        string= string[:pos] + new + string[pos+lengthNew:]
    print string

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
def mergeSort (arr): 
	#split array
	if len(arr)> 1:
		mid = len(arr)//2
		left = arr[:mid]
		right = arr[mid:]
		mergeSort(left)
		mergeSort(right)
		i=0
		k=0
		j=0
		while i <len(left) and j <len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i=i+1
			else: 
				arr[k] = right [j]
				j=j+1
			k=k+1
		#if anything is leftover, add from left[i]	
		while i < len(left):
			arr[k] = left[i]
			i+=1
			k+=1
		#if anything is leftover, add from right[j]
		while j <len(right):
			arr[k] = right[j]
			j+=1
			k+=1
	return arr

def runLength (string):
	if string is None or len(string)==0:
		return string
#create new string
	newString = []
	last_char = string[0]
	for index,char in enumerate(string[::2]):
		for i in range(char):
			newString.append(string[index*2+1])
	return newString

def main():
	arr1 = [7,1,5,2,3,6]
	arr2 = [3,8,6,20,7]
	m= len(arr1)//len(arr2)
	n= len(arr2)//len(arr1)