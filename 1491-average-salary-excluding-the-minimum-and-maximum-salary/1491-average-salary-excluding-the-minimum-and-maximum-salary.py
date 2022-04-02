class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        nl = salary[1:len(salary)-1]
        return sum(nl)/len(nl)