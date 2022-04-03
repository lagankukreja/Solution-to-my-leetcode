class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        
        if num==1:
            return True
        
        while(low<=high):
            
            mid = (low+high)//2
            if (mid*mid==num):
                return True      
            elif (mid*mid<num):
                low = mid+1
            else:
                high = mid-1
            print(mid)
        return False