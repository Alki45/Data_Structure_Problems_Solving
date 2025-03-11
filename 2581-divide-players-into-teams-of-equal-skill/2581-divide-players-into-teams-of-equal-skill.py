class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if(len(skill)==2):
            return skill[0]*skill[1]
        l,r=0,len(skill)-1
        count=-1
        skill.sort()
        skill_team={}
        target=skill[1]+skill[-2]
        while (l<r):
            if(skill[l]+skill[r]==target):
                skill_team[l]=tuple([skill[l],skill[r]])
            l+=1
            r-=1
        if(len(skill_team)==len(skill)/2):
            product=0
            for key,val in skill_team.items():
                product+=val[0]*val[1]
            return product
        return -1
