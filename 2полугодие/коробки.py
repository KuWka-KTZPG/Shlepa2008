with open('26.txt')as f:
    s=[int(x) for x in f]
    s.pop(0)
    s.sort(reverse=True)
    mini=s[0]
    k=1
    for i in range(1,len(s)):
        if s[i]-3>=mini:
            mini=s[i]
            k+=1
    print(mini, k)
