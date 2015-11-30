Insert front : Linked List -------------------------------
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
Delete Node : At Position ---------------------------------------------
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

Reverse Print -------------------------------------------------------
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

Reverse Linked List ------------------------------------------------------------------------------------------------------

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
  
---- MERGE TWO LINKED LISTS ----------------------------------------------------------------------------------
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
Get Node from pos from end ------------------------------------------------------------------------------------------
def GetNode(head, position):
    slow= head
    fast = head
    count = 0
    length= 0
    if head != None:
        while count < position:
            fast= fast.next
            count +=1
        while fast.next != None and slow.next != None:
                fast= fast.next
                slow= slow.next
    return slow.data
Copy a linked list with random pointer -----------------------------------------------------------------------------
Check if Linked List is acyclic -------------------------------------------------------------------------------------
def HasCycle(head):
    slow = head
    fast = head
    while fast != None:
        slow= slow.next
        if fast.next != None:
            fast=fast.next.next
        if slow == fast:
            return 1
        else: 
            return 0