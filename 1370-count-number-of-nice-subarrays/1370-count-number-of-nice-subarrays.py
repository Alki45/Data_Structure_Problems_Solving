class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def is_odd(num):
            if(num%2!=0):
                return True
        Odd_num=0
        count=0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        for num in nums:
            if(is_odd(num)):
                Odd_num+=1
            count += prefix_counts[Odd_num - k]
            prefix_counts[Odd_num] += 1
        return count
        

        