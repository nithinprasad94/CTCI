import time
import random

###WRITTEN CODE
##def solution(str):
##
##    dict chars = {}
##
##    repeat_flag = 0
##
##    for char in str:
##        if char not in keys():
##            char[key] = 1
##        else:
##            char[key] += 1
##            repeat_flag = 1
##            break
##
##    return repeat_flag

###WORKING CODE (NOT FULLY OPTIMIZED?)
def solution(str_in):

    chars = {}

    repeat_flag = 0

    for char in str_in:
        if char not in chars.keys():
            chars[char] = 1
        else:
            chars[char] += 1
            repeat_flag = 1
            break

    return repeat_flag

###WORKING CODE (AS IN BOOK - CONVERTED FROM JAVA TO PYTHON)
def solution2(str_in):
    if len(str_in) > 128: return 1 #128: largest unique char sequence size in ASCII
        
    chars = [0]*128

    for i in range(len(str_in)):
        val = ord(str_in[i])
        if chars[val]:
            return 1
        chars[val] = 1
    return 0

###TEST CASES

#Test Helper Function
def test():

    num_times = 200
    time_set_1 = []
    time_set_2 = []
    
    for h in range(1,num_times):
    
        str_list = []
        
        for i in range(200): #200 iterations of loop each time = 200 words
            num_chars = random.randint(1,200) #Random length string
            str_rand = ""
            for j in range(num_chars):
                str_rand = str_rand + chr(random.randint(0,127)) #ascii value of 0-127
            str_list.append(str_rand) #same as str_list += str_rand
            
        #print ""
        #print "TIME/EFFICIENCY TEST"
        #print "Solution 1"

        sub_time_set = []

        for test_str in str_list:
            start = time.time()
            solution(test_str)
            end = time.time()
            sub_time_set.append(end-start)
        
        time_set_1.append(sum(sub_time_set)/len(sub_time_set))
        
        #print "Time taken", end-start
        #print ""
        #print "Solution 2"
        sub_time_set = []

        for test_str in str_list:
            start = time.time()
            solution2(test_str)
            end = time.time()
            sub_time_set.append(end-start)
        
        time_set_2.append(sum(sub_time_set)/len(sub_time_set))
        
        #print "Time taken", end-start

    avg_time_1 = sum(time_set_1)/len(time_set_1)
    avg_time_2 = sum(time_set_2)/len(time_set_2)

    print("Average times for all solution 1 runs: ",avg_time_1)
    print("Average times for all solution 2 runs: ",avg_time_2)

def big_o_test():

    str_len_list = [2**i for i in range(0,8)] #Double word sizes
    time_set_1 = []
    time_set_2 = []
    
    for i in str_len_list:
    
        str_list = []
        
        for j in range(200000): #20000 words of size i
            num_chars = i #Length of string is i
            str_rand = ""
            for k in range(num_chars):
                str_rand = str_rand + chr(random.randint(0,127)) #ascii value of 0-127
            str_list.append(str_rand) #same as str_list += str_rand
            
        #print ""
        #print "TIME/EFFICIENCY TEST"
        #print "Solution 1"

        sub_time_set = []

        for test_str in str_list:
            start = time.time()
            solution(test_str)
            end = time.time()
            sub_time_set.append(end-start)
        
        time_set_1.append(sum(sub_time_set)/len(sub_time_set))
        
        #print "Time taken", end-start
        #print ""
        #print "Solution 2"
        sub_time_set = []

        for test_str in str_list:
            start = time.time()
            solution2(test_str)
            end = time.time()
            sub_time_set.append(end-start)
        
        time_set_2.append(sum(sub_time_set)/len(sub_time_set))
        
        #print "Time taken", end-start

    print("Average times for all solution 1 runs: ",time_set_1)
    print("Average times for all solution 2 runs: ",time_set_2)
    

print("\nBASIC TEST:")
print("Solution 1")
print(solution('$aph-.,'))
print(solution('alph'))
print(solution('alpha'))
print(solution('alphaq'))
print("Solution 2")
print(solution('$aph-.,'))
print(solution('alph'))
print(solution('alpha'))
print(solution('alphaq'))

print("\nRANDOM TEST:")
test()

print("\nBIG_O_TEST:")
big_o_test()
