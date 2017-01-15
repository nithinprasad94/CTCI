###WRITTEN CODE
##def solution(M):
##
##    n = len(M)
##
##    new_M = [[0]*n]*n
##
##    num_layers = n/2
##    odd = n%2 #handles potential middle element
##
##    for i in range(num_layers):
##        start = i-1
##        end = n - i - 1
##
##        for j in range(start,end+1):
##
##            new_M[j][end] = M[start][j]
##            new_M[end][n-j] = M[j][end]
##            new_M[n-j][start] = M[end][n-j]
##            new_M[start][j] = M[n-j][start]
##
##    if odd:
##        new_M[num_layers + odd][num_layers + odd] = M[num_layers + odd][num_layers + odd]

###WORKING CODE (UNOPTIMIZED)
def solution(M):

    n = len(M)

    new_M = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        new_M.append(temp)
    
    #print_matrix(new_M)

    num_layers = int(n/2)
    odd = n%2 #handles potential middle element

    for i in range(1,num_layers+1): #Iterate through layer no. 1 to num_layers
        #print "layer: ",i    
        
        start = i-1
        end = n-1 - (i-1)

        #print start
        #print end
        #print range(start,end+1)
        for j in range(start,end): #Only go to end-1
            new_M[j][end] = M[start][j]
            #print_matrix(new_M)
            new_M[end][n-j-1] = M[j][end]
            #print_matrix(new_M)
            new_M[n-j-1][start] = M[end][n-j-1]
            #print_matrix(new_M)
            new_M[start][j] = M[n-j-1][start]
            #print_matrix(new_M)
            
    if odd:
        new_M[num_layers][num_layers] = M[num_layers][num_layers]        
    return new_M

#WORKING CODE(TEXT SOLUTION - OPTIMIZED)
def solution2(M):

    n = len(M)
   
    num_layers = n/2

    for i in range(1,num_layers+1): #Iterate through layer no. 1 to num_layers
        #print "layer: ",i    
        
        start = i-1
        end = n-1 - (i-1)

        for j in range(start,end): #Only go to end-1
            temp = M[start][j] #This value is used in the last of the 4 moves
            M[start][j] = M[n-j-1][start]
            M[n-j-1][start] = M[end][n-j-1]
            M[end][n-j-1] = M[j][end]
            M[j][end] = temp
             
    return M

###TEST CASES
#Helper function
def print_matrix(M):

    n = len(M)

    for i in range(n):
        line = ""
        for j in range(n):
            line += str(M[i][j]) + " "
        print(line)
    print("-------------")

    return

#Test cases
M1 = [[1,2,3],[4,5,6],[7,8,9]]
M2 = [[1,2,3,4],[5,6,7,8],[9,1,2,3],[4,5,6,7]]
M3 = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9]]
print_matrix(M1)
print_matrix(M2)
print_matrix(M3)
M1_rot = solution(M1)
M2_rot = solution(M2)
M3_rot = solution(M3)
print_matrix(M1_rot)
print_matrix(M2_rot)
print_matrix(M3_rot)

M1 = [[1,2,3],[4,5,6],[7,8,9]]
M2 = [[1,2,3,4],[5,6,7,8],[9,1,2,3],[4,5,6,7]]
M3 = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9]]
M1_rot2 = solution2(M1)
M2_rot2 = solution2(M2)
M3_rot2 = solution2(M3)
print_matrix(M1_rot2)
print_matrix(M2_rot2)
print_matrix(M3_rot2)



