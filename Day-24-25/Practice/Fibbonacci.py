def fibbo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n+fibbo(n-1)
n=int(input("Enter the number:"))
print(fibbo(n))