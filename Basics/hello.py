1_merging sorted arrays:
n=int(input())
t=list(map(int,input().split()))
m=int(input())
p=list(map(int,input().split()))
i=0
j=0
while(i<n and j<m):
     if(t[i]<p[j]):
        print((t[i]),end="")
        i+=1
     else:
        print((p[j]),end="")
        j=j+1

    
        
