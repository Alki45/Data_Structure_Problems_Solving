class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict=Counter(nums1)
        result=[]

        for i in nums2:
            if nums1_dict[i] > 0:
                result.append(i)
                nums1_dict[i]-=1
        return result
        