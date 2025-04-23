class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        for i in logs:
            if i.startswith('..') and count>0:
                count-=1
            elif i.startswith('.'):
                count=count
            else:
                count+=1
        return count