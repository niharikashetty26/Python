num=65
for i in range(1,5):
    for j in range(i,0,-1):
        ch=chr(num)
        print(ch,end="")
        num=num+1
    print()