def solution(s1, s2):
    characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ans1 = {}
    ans2 = {}
    for i in s1:
        if i in ans1.keys():
            ans1[i]+=1
        else :
            ans1[i]=1
    for i in s2:
        if i in ans2.keys():
            ans2[i]+=1
        else:
            ans2[i]=1
    ans = 0
    for item in ans1.keys():
        if item in ans2.keys() :
            ans += min(ans1[item],ans2[item])
    return ans
            
    
        

