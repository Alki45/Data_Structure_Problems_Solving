class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = []
        freq_count = Counter(nums)

        def dfs():
            if len(permutation) == len(nums) :
                result.append(permutation.copy()) 
                return
            for n in freq_count :
                if freq_count[n] > 0:
                    permutation.append(n)
                    freq_count[n] -=1

                    dfs()

                    freq_count[n] +=1
                    permutation.pop()
        dfs()
        return result


