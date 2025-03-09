class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sort=list(s)
        s_sort.sort()
        t_sort=list(t)
        t_sort.sort()
        if(s_sort==t_sort):
            return True
        return False
        