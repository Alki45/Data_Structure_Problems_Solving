class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
                i=0
        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        """
        """        left,right,i=0,0,0
        while left<m and right <n:
            if(nums1[left]<nums2[right]):
                nums1[i]=nums1[left]
                left+=1
            else:
                nums1[i],nums2[right]=nums2[right],nums1[left]
                right+=1
            i+=1"""
        for i in range(len(nums2)):
                nums1.append(nums2[i])
        nums1.sort()
        for i in range (n):
                nums1.remove(0)
            

