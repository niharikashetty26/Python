s="abc"
length=len(s)
a=list(s)
print(a)
def format_str(List):
    return "".join(List)
def find_permutations(a,i,length):
    if i==length:
        print(format_str(a))
    else:
        for j in range(i,length):
            print(a[i])
            print(a[j])
            a[i],a[j]=a[j],a[i]
            find_permutations(a,i+1,length)
            a[i],a[j]=a[j],a[i]


find_permutations(a,0,length)

