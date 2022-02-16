'''
firstly we are making the number of possible subsequences of a string 
then we are solving it 
 solve will count the number of arrays that can form a palindrome 
 
 formspalindrome checks if the array can form palindrome or not 
 
 
 
'''

def subArray(arr, n):
    answer = []
    for i in range(0,n):
        for j in range(i+1,n+1):
            answer.append(arr[i:j])
    return answer      
def solve(arr):
    def formspalindrome(item):
        ans = dict()
        lst = list(set(list(item)))
        for i in lst:
            ans[i] = 0
        for i in item :
            ans[i]+=1
        count = 0 
        for i in ans.values():
            if i%2==1 :
                count+=1
                if count ==2 :
                    return False
        return True
    ans = 0
    for i in arr:
        if formspalindrome(i):
            ans+=1
    print(ans)
arr = list(input())
ans = []
i = 0
tot = subArray(arr,len(arr))
solve(tot)
'''
but later i thought it could further be reduced and the solution is as below 
'''

def subArray(arr, n):
    answer = 0
    def formspalindrome(item):
        ans = dict()
        lst = list(set(list(item)))
        for i in lst:
            ans[i] = 0
        for i in item :
            ans[i]+=1
        count = 0 
        for i in ans.values():
            if i%2==1 :
                count+=1
                if count ==2 :
                    return False
        return True
    for i in range(0,n):
        for j in range(i+1,n+1):
            if formspalindrome(arr[i:j]):
                answer+=1
    return answer      
arr = list(input())
ans = []
i = 0
print( subArray(arr,len(arr)))




