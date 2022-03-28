class Solution:
    def twoSum(self, nums, target) :
        seen = {}
        for i, b in enumerate(nums):
            # a + b = target -> a = target - b
            a = target - b
            if a in seen:
                return [seen[a], i]
            seen[b] = i