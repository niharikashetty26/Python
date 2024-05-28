def replace(s,a,b):
    if len(s)==0:
        return ""
    small_output=replace(s[1:],a,b)
    if s[0]==a:
        return b+small_output
    else:
        return s[0]+small_output
ans=replace("asdasaaa","a","b")
print(ans)