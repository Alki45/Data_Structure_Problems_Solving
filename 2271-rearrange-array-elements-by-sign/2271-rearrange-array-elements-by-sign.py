class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positiv=[]
        negative=[]
        for i in nums:
            if(i>=0):
                positiv.append(i)
            else:
                negative.append(i)
        for i in range(len(nums)):
            if(i%2==0):
                nums[i]=positiv[i//2]
            else:
                nums[i]=negative[i//2]
        return nums