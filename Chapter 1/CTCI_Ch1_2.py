###WRITTEN CODE
##def solution(str1,str2):
##
##    if len(str1) == len(str2) == 0:
##        return 1 #assume empty string permutes itself
##
##    if len(str1) != len(str2):
##        return 0 #Not a perm if not the same length
##
##    num_chars_ascii = 128
##    arr1 = [0]*128
##    arr2 = [0]*128
##
##    for i in range(str1):
##        char1 = str1[i]
##        char2 = str2[i]
##
##        val1 = ord(char1)
##        val2 = ord(char2)
##
##        arr1[val1] += 1
##        arr2[val2] += 1
##
##    for i in range(num_chars_ascii):
##        if (arr1[i] != arr2[i]):
##            return 0 #is not perm
##
##    return 1 #is perm

###WORKING CODE (NOT FULLY OPTIMIZED)
def solution(str1,str2):

    if len(str1) == len(str2) == 0:
        return 1 #assume empty string permutes itself

    if len(str1) != len(str2):
        return 0 #Not a perm if not the same length

    num_chars_ascii = 128
    arr1 = [0]*num_chars_ascii
    arr2 = [0]*num_chars_ascii

    for i in range(len(str1)):
        char1 = str1[i]
        char2 = str2[i]

        val1 = ord(char1)
        val2 = ord(char2)

        arr1[val1] += 1
        arr2[val2] += 1

    for i in range(num_chars_ascii):
        if (arr1[i] != arr2[i]):
            return 0 #is not perm

    return 1 #is perm

###WORKING CODE (TEXT SOLUTION 1)
def sort(str_in):
    return ''.join(sorted(str_in))

def solution1(str1,str2):

    if sort(str1) == sort(str2):
        return 1 #Is not perm
    return 0 #Is perm

###WORKING CODE (TEXT SOLUTION 2)
def solution2(str1,str2):

    if len(str1) == len(str2) == 0:
        return 1 #assume empty string permutes itself

    if len(str1) != len(str2):
        return 0 #Not a perm if not the same length

    num_chars_ascii = 128
    arr = [0]*128
    
    for char in str1:
        
        val = ord(char)
        
        arr[val] += 1
        
    for char in str2:

        val = ord(char)

        arr[val] -= 1

        if (arr[val] < 0):
            return 0
        
    return 1 #is perm

###TEST CASES
print("MY SOLUTION:")
print(solution("",""))
print(solution("","alpha"))
print(solution("happy","pahpy"))
print(solution("fappy","happy"))
print(solution("fap","fappy"))
print("\nTEXT SOLUTION 1:")
print(solution1("",""))
print(solution1("","alpha"))
print(solution1("happy","pahpy"))
print(solution1("fappy","happy"))
print(solution1("fap","fappy"))
print("\nTEXT SOLUTION 2:")
print(solution2("",""))
print(solution2("","alpha"))
print(solution2("happy","pahpy"))
print(solution2("fappy","happy"))
print(solution2("fap","fappy"))
