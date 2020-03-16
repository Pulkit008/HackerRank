def print_rangoli(n):
    mx=96+n
    for i in list(range(1,n+1))+list(range(n-1,0,-1)):
        print( ('-'.join([chr(x) for x in range(mx,mx-i,-1)]+[chr(x) for x in range(mx+2-i,mx+1)])).center(4*(n-1)+1,'-') )
