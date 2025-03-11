class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if(len(skill)==2):
            return skill[0]*skill[1]
        l,r=0,len(skill)-1
        count=-1
        skill.sort()
        skill_team={}
        target=skill[1]+skill[-2]
        product=0
        while (l<r):
            if(skill[l]+skill[r]==target):
                product+=skill[l]*skill[r]
            else:
                return -1
            l+=1
            r-=1
        return product
