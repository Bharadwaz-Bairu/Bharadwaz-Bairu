n = int(input())
for i in range(n):
    m = int(input())
    ans = []
    print("Test Case #"+str(i+1)+":")
    for i in range(m):
        arr = list(map(int,input().split()))
        ans.insert(0,arr)

    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[j][i],end = " ")
        print()
