class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        merged = {}

        start, end = intervals[0]

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]

            if curr_start <= end: 
                end = max(end, curr_end) 
            else: 
                merged[start] = end
                start, end = curr_start, curr_end 
        merged[start] = end

        result=[[key,value] for key,value in merged.items()]

        return result