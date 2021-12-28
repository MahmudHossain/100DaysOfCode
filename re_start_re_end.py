s=input()
k=input()
k_len=len(k)
flag=0
for i in range(len(s)):
    if k==s[i:i+k_len]:
        flag=1
        print('('+str(i)+', '+str(i+k_len-1)+')')
if flag==0:
    print((-1, -1))