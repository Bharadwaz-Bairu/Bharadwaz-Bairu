class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        length = len(s)
        arr = 0
        temp = ""
        while i < length:
            if s[i] not in temp:
                temp += s[i]
            else :
                if len(temp) > arr :
                    arr = len(temp)
                temp= temp[temp.index(s[i])+1:]+s[i]
            i+=1
        if len(temp) > arr:
            arr = len(temp)
        return arr
        
            
        
