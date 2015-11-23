String: Count total number of each unique element in string-----------------------------------------------------------------
from collections import Counter 
def counting(in_string):
	encoded_string=""
	letter_count = Counter(in_string)
	for key in letter_count:
		val = str(letter_count[key])
		encoded_string += val+key
		print(encoded_string)
	return encoded_string

def counting(in_string):
	encoded_string=""

String: Compress string-----------------------------------------------------------------------------------------------
def compress_string(string):
    if string is None or len(string) == 0:
        return string

    # Calculate the size of the compressed string
    size = 0
    last_char = string[0]
    for char in string:
        if char != last_char:
            size += 2
            last_char = char
    size += 2

    # If the compressed string size is greater than
    # or equal to string size, return original string
    if size >= len(string):
        return string

    # Create compressed_string
    compressed_string = list()
    count = 0
    last_char = string[0]
    for char in string:
        if char == last_char:
            count += 1
        else:
            compressed_string.append(last_char)
            compressed_string.append(str(count))
            count = 1
            last_char = char
    compressed_string.append(last_char)
    compressed_string.append(str(count))

    # Convert the characters in the list to a string
    return "".join(compressed_string)


String: Print Reverse-----------------------------------------------------------------
def printReverse(input, num_array):
    woohoo=""
    for i in reversed(num_array[:input]):
        woohoo+=i+" "
    for i in num_array[input:]:
        woohoo+=i+" "
    print woohoo[:-1]

input=int(raw_input())
num_array=[]
n = raw_input()
num_array=n.split(" ")
printReverse(input, num_array)

String: All Permutations of string -------------------------------------------------------------
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

String: All Permutations of string with list comp ---------------
def listCompPermute (num):
	## len(num) < 1 , return [[]]
	## insert each new value into possible interspaces
	##which there are n+1 of them  if there are n chars already 
	results =[[]]
	for x in num:
		results = [r[:i] +[x] + r[i:] for r in results for i in range (len(r)+1)]
	return results
Cipher : -----------------------------------------------------------------------
class Solution(object):
    def solve(self, cipher):
        """
        similar to next permutation
        :param cipher: the cipher
        """
        A = list(cipher)
        A = map(ord, A)
        n = len(A)

        a = -1
        for i in xrange(n - 1, 0, -1):
            if A[i - 1] < A[i]:
                a = i - 1
                break
        else:
            return "no answer"

        b = -1
        for i in xrange(n - 1, a, -1):
            if A[i] > A[a]:
                b = i
                break
        else:
            return "no answer"

        A[a], A[b] = A[b], A[a]  # swap
        A = A[:a + 1] + A[n - 1:a:-1]  # reverse
        return "".join(map(chr, A))


if __name__ == "__main__":
    import sys

    #f = open("1.in", "r")
    f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = f.readline().strip()

        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,

String: Find a certain pattern in a string and replace --------------------------------------------------------------------------
String: Convert char string to an int --------------------------
Array: Find frequency of number in sorted array ----------------
Array: Implement a linked list using arrays ------------------
Arrays: Merge n sorted arrays ----------------------------------
Set: Implement iterator for a set -------------------------------
String: Find substring in string -------------------------------------
Array: Find kth element in reunion of two sorted arrays -----------
