for i in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    m=int(input())
    my=[]
    pf,c=0,0
    q=[]
    for i in range(n):
        z=a[i]
        if z not in my:
            if len(my)<m:
                my.append(z)
            else:
                my[my.index(q.pop(0))]=z
            pf+=1
        else:
            q.remove(z)
        q.append(z)    
    print(pf)

        
