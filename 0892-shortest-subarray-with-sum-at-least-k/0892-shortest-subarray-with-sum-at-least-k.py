class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        result = n + 1
        dq = deque()
        
        for j in range(n + 1):

            while dq and prefix[j] - prefix[dq[0]] >= k:
                result = min(result, j - dq.popleft())

            while dq and prefix[j] <= prefix[dq[-1]]:
                dq.pop()
            
            dq.append(j)
        if result <= n:
            return result
        return -1
