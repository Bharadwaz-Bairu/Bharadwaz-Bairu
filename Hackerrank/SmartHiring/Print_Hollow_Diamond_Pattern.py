n = int(input())
for i in range(n):
    m = int(input())
    print("Case #"+str(i+1)+":")
    for i in range(m):
        for j in range(m):
            if i+j == m//2 or i+j == m//2 + 2*i or m-i+j == m//2+1 or i+j == m+m//2-1  :
                print('*',end = "")
            else :
                print(" ",end = "")
        print()
    
