class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        Freq_num=Counter(nums)
        n=len(nums)
        res=[]
        
        for key, value in Freq_num.items():
            if(value>n/3):
                res.append(key)
        return res