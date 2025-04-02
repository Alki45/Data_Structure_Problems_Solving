class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Dict_num=Counter(nums)
        Max_freq=0
        major=0
        for key,value in Dict_num.items():
            Max_freq=max(Max_freq,value)
            if(Max_freq==value):
                major=key
        return major