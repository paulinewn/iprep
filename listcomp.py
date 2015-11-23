List: Flatten a list of lists----------------------------------------------------------------------------------------------
[x for row in matrix for x in row]
String: All Permutations of string with list comp --------------------------------------------------------------------------
def listCompPermute (num):
	## len(num) < 1 , return [[]]
	## insert each new value into possible interspaces
	##which there are n+1 of them  if there are n chars already 
	results =[[]]
	for x in num:
		results = [r[:i] +[x] + r[i:] for r in results for i in range (len(r)+1)]
	return results