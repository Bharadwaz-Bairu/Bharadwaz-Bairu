import math

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        if length <= 2 :
            if 1 not in flowerbed and n<=1:
                return True
            if n < 1  :
                return True
            else :
                return False 
        item = 0
        arr = []
        i = 0 
        while i < length :
            if flowerbed[i] == 0 :
                if i==0 or i== length-1:
                    item+=1
                    
                item += 1

            if flowerbed[i] == 1 :
                arr.append(item)
                item = 0
            i+=1
        arr.append(item)
        ans = 0 
        for i in range(len(arr)):
            if arr[i] >=3 :
                ans += (math.ceil(arr[i]/2)-1)
        temp = False
        if ans >= n :
            temp = True

        return temp


            
            
