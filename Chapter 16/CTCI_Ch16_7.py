def cust_max(a,b):

    sign_one = (a-b)//abs(a-b)
    #print(sign_one)
    #print((sign_one+1)*a//2)
    #print((sign_one-1)*b//(-2))
    print((sign_one+1)*a//2 + (sign_one-1)*b//(-2))

cust_max(3,7)
cust_max(7,3)
