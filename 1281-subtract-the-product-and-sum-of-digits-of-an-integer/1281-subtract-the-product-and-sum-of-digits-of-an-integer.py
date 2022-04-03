class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum = 0
        while n > 0:
            num = n % 10
            n = int(n / 10)
            prod *= num
            sum += num
        return prod - sum