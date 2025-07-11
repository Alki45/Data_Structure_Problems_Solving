class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_frq=Counter(nums)
        res = [key for key,value in dict_frq.items()]
        sorted_val = sorted(dict_frq.items(), key=lambda x: x[1], reverse=True)
        #print(sorted_val)
        res = [item[0] for item in sorted_val[:k]]
        return res

        