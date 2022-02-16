'''
In this program what we are doing is if the smallest element has the same index
with the other one in the ans dictionary then we are replacing the smallest element
with the biggest element in the array and thus we get the values of smallest elements from each line consecutively and 
solution is continued



'''


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
