class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort(reverse = True)
        diff = arr[0]-arr[1]
        if len(arr)== 2:
            return True
        i = 1
        while i<len(arr)-1:
            
            if arr[i]-arr[i+1] != diff:
                return False
            i +=1
        return True
                