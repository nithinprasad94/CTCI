class Node(object):
    value = 0
    seq = None

    def __init__(self,val,ptr):
        self.value = val
        self.seq = ptr

###WRITTEN CODE (NOT WORKING)
##def solution(head):
##
##    if head == None:
##        return None
##    print "head",head.value
##
##    seen_values = {}
##
##    seen_values[curr.value] = 1
##    curr = head
##
##    while(curr.seq != None):
##
##        if curr.value in dict.keys():
##            curr.seq = curr.seq.seq
##        else:
##            seen_values[curr.value] = 1
##
##        curr = curr.seq
##
##    return head

###WORKING CODE (NOT OPTIMIZED)
def solution(head):

    if head == None:
        return None
    #print "head",head.value

    seen_values = {}

    curr = head
    seen_values[curr.value] = 1
    #print seen_values
    #print "seq to head", curr.seq.value
    #print type(curr)

    while curr.seq != None:
        #print curr.value
        
        if curr.seq.value in seen_values.keys():
            seen_values[curr.seq.value] += 1
            curr.seq = curr.seq.seq
        else:
            seen_values[curr.seq.value] = 1
            curr = curr.seq
        #print seen_values

###WORKING CODE (TEXT SOLUTION)
def solution2(n):

    vals = {}
    
    prev = None

    while (n != None):
        if (n.value in vals.keys()):
            prev.seq = n.seq
        else:
            vals[n.value] = 1
            prev = n
        n = n.seq

###WORKING CODE (TEXT SOLUTION - NO BUFFER ALLOWED)
def solution3(n):

    curr = n

    while (curr != None):

        runner = curr

        while (runner.seq != None):
            if (runner.seq.value == curr.value):
                runner.seq = runner.seq.seq
            else:
                runner = runner.seq

        curr = curr.seq

###TESTER
#Helper Functions/Classes
def print_nodes(head):

    curr = head
    #print curr.value

    if curr == None:
        return

    line = ""

    while (curr != None):
        #print curr.value
        line += str(curr.value)

        
        if (curr.seq != None):
            #print "here"
            line += " -> "

        curr = curr.seq

    print(line)

#Test Case
a = Node(1,None)
b = Node(2,a)
c = Node(3,b)
d = Node(2,c)
e = Node(4,d)
f = Node(1,e) #Treat as head

#print f.value
#print f.seq.value
#print f.seq.seq.value

print("Testing ...")
print_nodes(f)

solution(f)
print_nodes(f)

a = Node(1,None)
b = Node(2,a)
c = Node(3,b)
d = Node(2,c)
e = Node(4,d)
f = Node(1,e) #Treat as head

print_nodes(f)
solution2(f)
print_nodes(f)

a = Node(1,None)
b = Node(2,a)
c = Node(3,b)
d = Node(2,c)
e = Node(4,d)
f = Node(1,e) #Treat as head

print_nodes(f)
solution3(f)
print_nodes(f)




        
