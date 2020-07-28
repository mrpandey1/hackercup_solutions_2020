temp='YNNYY'#in
temp2='YYYNY'#out
def ans(temp,temp2):
    a=[['N']*len(temp) for i in range(1,len(temp)+1)]
    for i in range(len(temp)):
        a[i][i]='Y'
    for i in range(len(temp)):
        for j in range(len(temp)):
            if i==j:
                a[i][j]=='Y'
            else:
                if abs(i-j)==1:
                    if temp2[i]=='Y' and temp[j]=='Y':
                        a[i][j]='Y'
                    else:
                        a[i][j]='N'
                else:
                    if temp[j]=='N' or temp2[i]=='N':
                       a[i][j]='N'
                    else:
                        flag=True
                        if i<j:
                            for l in range(i+1,j):
                                if temp[l]=='N' or temp2[l]=='N':
                                    flag=False
                        else:
                            for l in range(i-1,j,-1):
                                if temp[l]=='N' or temp2[l]=='N':
                                    flag=False
                        if flag==False:
                            a[i][j]='N'
                        else:
                            a[i][j]='Y'
                             
    return a
main=[]
for i in range(int(input())):
    leng=int(input())
    temp=input()
    temp2=input()
    main.append(ans(temp,temp2))
count=1
for i in main:
    print(f'Case #{count}:')
    for j in i:
        print(''.join(j))
    count+=1
