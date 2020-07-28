def ans(temp):
    if len(set(temp))==1:
        return 'N'
    i=0
    while i<len(temp):
        if temp=='A' or temp=='B':
            return 'y'
        if len(set(temp[i:i+3]))==1:
            i+=1
            continue
        else:
            a=temp[i:i+3].count('A')
            b=temp[i:i+3].count('B')
            if a>b:
                temp=f'{temp[0:i]}A{temp[i+3:]}'
            else:
                temp=f'{temp[0:i]}B{temp[i+3:]}'
            i=0
    return 'n'
res=[]
for i in range(int(input())):
    leng=int(input())
    temp=input()
    res.append(ans(temp))
for i in range(1,len(res)+1):
    print(f'Case #{i}: {res[i-1].upper()}')
