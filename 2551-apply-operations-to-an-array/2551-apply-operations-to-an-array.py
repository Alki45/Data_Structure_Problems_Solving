class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(1,len(nums)):
            if(nums[i-1]==nums[i]):
                nums[i-1]=nums[i-1]*2
                nums[i]=0
            else:
                continue
        for i in range(len(nums)):
            if(nums[i]>0):
                result.append(nums[i])
                print(nums[i])
            else:
                continue
        for i in range(len(result),len(nums)):
            result.append(0)
        return result
        