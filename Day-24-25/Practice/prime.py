def is_prime(n):
    if n>2:
        for i in range(2, n):
            if n%i==0:
                return False
            else:
                return True
    elif n==1 or n==2:
        return True
    # else:
    #     return True
n=int(input("Enter the number:"))
print(is_prime(n))