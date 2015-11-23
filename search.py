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