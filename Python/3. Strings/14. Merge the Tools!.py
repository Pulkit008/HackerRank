def merge_the_tools(s, k):
    for i in range(0,len(s),k):
        print( ''.join(dict.fromkeys(s[i:i+k])) )
