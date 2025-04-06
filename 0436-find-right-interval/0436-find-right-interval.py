class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        result=[]
        interval_index=[(interval[0],interval[1], i) for i,interval in enumerate(intervals)]
        inteval_sorted=sorted(interval_index, key=lambda x:x[0])
        for interval in intervals:
            end=interval[1]
            flag=False
            for start, i,index in inteval_sorted:
                if(start>=end):
                    result.append(index)
                    flag=True
                    break
            if(flag==False):
                result.append(-1)
        return result