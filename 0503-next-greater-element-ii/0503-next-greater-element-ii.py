class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dict_ = defaultdict(lambda: -1)
        stack = []

        for i in range(2 * n):
            num = nums[i % n] 

            while stack and nums[stack[-1]] < num:
                top_idx = stack.pop()
                dict_[top_idx] = num

            if i < n: 
                stack.append(i)

        result = [dict_[i] for i in range(n)]
        return result