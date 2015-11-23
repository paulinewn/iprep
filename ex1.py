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