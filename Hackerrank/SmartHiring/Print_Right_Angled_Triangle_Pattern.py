n = int(input())
for k in range(n):
    m = int(input())
    print('Case #'+str(k+1)+":")
    for i in range(m):
        for j in range(m-i-1):
            print(" ",end = "")
        for j in range(m-i-1,m):
            print("*",end="")
        print()
