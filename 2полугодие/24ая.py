with open('24.txt')as f:
    s=f.readline().replace('C','s').replace('D','s').replace('F','s')
    s=s.replace('A','g').replace('O','g')
    s=s.replace('sg','*')
    kmax=0
    cnt=0
    for i in range(len(s)):
        if s[i]=='*':
            cnt+=1
            kmax=max(kmax,cnt)
        else:
            cnt=0
    print(kmax)
