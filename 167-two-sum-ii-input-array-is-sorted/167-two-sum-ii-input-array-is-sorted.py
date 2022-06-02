class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length_number = len(numbers)
        i,j = 0,length_number-1
        
        while (i<j ):
            sum_rq =numbers[i]+numbers[j]
            if sum_rq > target:
                j = j-1
            elif sum_rq< target:
                i = i +1
            else:
                return [i+1,j+1]

        