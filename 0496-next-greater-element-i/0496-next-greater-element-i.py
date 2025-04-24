class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_=defaultdict(lambda:-1)
        stack=[]
        for num in nums2:
            while stack and stack[-1]<num:
                top=stack.pop()
                dict_[top]=num
            stack.append(num)
        result=[dict_[num] for num in nums1]
        return result
            
        
            
        