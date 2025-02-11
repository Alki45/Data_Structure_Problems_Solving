class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_map = Counter()
        for a in nums1:
            for b in nums2:
                sum_map[a + b] += 1
        
        # Step 2: Check sums for nums3 and nums4
        count = 0
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in sum_map:
                    count += sum_map[target]
        
        return count