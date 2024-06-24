def is_Prime(n):
    if n==1 or n==2:
        print(n)
    else:
        for i in range(2,(n//2)+1):
            if n%2!=0:
                print(i)

    return


n=int(input("Enter the number: "))
print(is_Prime(n))