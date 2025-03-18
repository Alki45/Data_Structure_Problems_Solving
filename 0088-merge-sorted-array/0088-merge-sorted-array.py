class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        left,right,i=0,0,0
        temp=nums1[:m]
        print(temp)
        while left<m and right <n:
            if(temp[left]<nums2[right]):
                nums1[i]=temp[left]
                left+=1
            else:
                nums1[i]=nums2[right]
                right+=1
            i+=1
        while right<n:
                nums1[i]=nums2[right]
                right+=1
                i+=1
        while left<m:
                nums1[i]=temp[left]
                left+=1
                i+=1




