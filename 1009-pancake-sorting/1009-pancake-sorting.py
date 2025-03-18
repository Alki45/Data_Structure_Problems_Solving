class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for x in range(len(arr), 1, -1):
            i = arr.index(x)
            res.extend([i + 1, x])
            print('Res',res)
            arr= arr[:i:-1] + arr[:i]
            print(arr)
        return res
                    
        