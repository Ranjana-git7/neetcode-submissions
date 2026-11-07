class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        r = sorted(s)
        k = sorted(t)
        if r==k:
            return True 
        else:
            return False 