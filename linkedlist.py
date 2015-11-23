------INSERT FRONT LINKED LIST -----
def Insert (head, data):
    temp = Node(data)
    if head is None:
        head = temp
        return head
    else: 
        temp.next = head
        head = temp
        current =head
        while (current.next != None):
            current= current.next
        return head
------DELETE NODE AT POSITION -------
def Delete(head, position):
    place = 0
    if head is None:
        return head
    current = head 
    while current != None:
        if (position==0):
            head = head.next
            break
        elif (place == position -1):
            current.next=current.next.next
            break
        else:
            place +=1
            current=current.next 
    return head

----------- REVERSE PRINT LL ----------
ITERATIVE
def ReversePrint(head):
    length=0
    if head is None:
        return head
    current = head
    reverseprint= []
    while current != None: 
       if current.data != None:
           reverseprint.insert(0,current.data)
       current = current.next
       length+=1
    print reverseprint

RECURSION
def ReversePrint(head):
    if head:
        ReversePrint(head.next)
        print head.data
        
def stringconv(A):
    string =""
    for i in A:
        char = str(i)
        string += char+"\n"
    print string

--------- REVERSE LINKED LIST ----------

#Iterative
def Reverse(head):
  last = None
  current = head

  while(current is not None):
    nxt = current.next
    current.next = last 
    last = current
    current = nxt

  return last

#Recursive
def recurse(head,last):
  if head is None:
    return last
  nxt = n.next
  n.next = last
  return reverse(nxt, head)
  
---- MERGE TWO LINKED LISTS -------------------------
----- RETURN DEEPEST NODE IN B TREE -----------------
Copy a linked list with random pointer -----------------