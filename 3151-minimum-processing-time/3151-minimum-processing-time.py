class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        excutiontime=[]
        max_=0
        for i in range(0,len(tasks),4):
            excutiontime.append(tasks[i:i+4])
        processorTime.sort(reverse=True)
        for i in range(len(processorTime)):
            max_=max(processorTime[i]+max(excutiontime[i]),max_)
        return max_
