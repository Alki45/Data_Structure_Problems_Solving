class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for x in range(left, right + 1):
            Result = False
            for start, end in ranges:
                if (start <= x and x <= end):
                    Result = True
                    break
            if not Result:
                return False
        return True
            