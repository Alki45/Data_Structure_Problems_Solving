class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Dict_num=Counter(nums)
        Max_freq=0
        for key,value in Dict_num.items():
            Max_freq=max(Max_freq,value)
        for key,value in Dict_num.items():
            if(Dict_num[key]==Max_freq):
                return key
        