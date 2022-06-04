class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        length = int(n/2) + 1
        print(length)
        for i in range(1,length ):
            
            res.append(i*1)
            res.append(i*-1)
            
        if n%2 != 0:

            res.append(0)

        return res