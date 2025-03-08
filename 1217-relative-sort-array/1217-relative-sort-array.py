class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        diff_arr=[i for i in arr1 if i not in arr2]
        diff_arr.sort()
        result=[]
        for i in arr2:
            for j in range(arr1.count(i)):
                result.append(i)

        return (result+diff_arr)
        