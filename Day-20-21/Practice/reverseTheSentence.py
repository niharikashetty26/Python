S = "i.like.this.program.very.much"
ans=S.split(".")
# print(ans)
i=0
j=len(ans)-1
while(i<=j):
    ans[i],ans[j]=ans[j],ans[i]
    i=i+1
    j=j-1
print(".".join(ans))