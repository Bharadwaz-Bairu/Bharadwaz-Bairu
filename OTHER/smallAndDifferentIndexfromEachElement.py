def solve(arr):
    ans = {arr[0].index(min(arr[0])):min(arr[0])}
    for i in range(1,len(arr)):
        while arr[i].index(min(arr[i])) in ans.keys():
            arr[i][arr[i].index(min(arr[i]))] = max(arr[i])+1
        ans[arr[i].index(min(arr[i]))] = min(arr[i])
    print(sum(ans.values()))
    
n = int(input())
arr = []
for i in range(n):
    temp = list(map(int,input().split()))
    arr.append(temp)
solve(arr)
