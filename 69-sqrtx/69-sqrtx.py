class Solution:
    def mySqrt(self, x: int) -> int:
        ans = -1
        if x == 0:
            ans = 0
        if x == 1:
            ans = 1
        left = 0
        right = x
        while (left<=right):
            mid = (left +right)//2
            
            if(mid*mid==x):
                return mid
            elif(mid*mid<x):
                ans = mid
                left = mid+1
                
            else:
                right = mid-1
            print(mid)
        return ans