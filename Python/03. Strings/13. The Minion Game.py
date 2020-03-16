def minion_game(sr):
    v='AEIOU'
    k,s=0,0
    for i in range(len(sr)):
        if sr[i] in v:
            k+=len(sr)-i
        else:
            s+=len(sr)-i
    if k>s:
        print("Kevin", k)
    elif k<s:
        print("Stuart", s)
    else:
        print("Draw")
