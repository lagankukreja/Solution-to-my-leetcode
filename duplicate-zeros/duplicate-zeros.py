class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        '''
        Input: arr = [1,0,2,3,0,4,5,0]
        Output: [1,0,0,2,3,0,0,4]
        '''
        length = len(arr)
        i = 0
        while(i<length):
            if arr[i] == 0:
                arr.insert(i+1,0)
                arr.pop(-1)
                i = i+2
                
            else:
                i = i+1
        
        return arr