class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = list()
        for x in s: 
            if x.isalpha()== True or x.isnumeric()== True:
                a.append(x.lower())
        if a == a[::-1]:
            return True
        return False
                