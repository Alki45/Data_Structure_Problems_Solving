class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        warm_day=[0]*n
        stack=[]
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                top=stack.pop()
                warm_day[top]=i-top
            stack.append(i)
        return warm_day


        
            
        