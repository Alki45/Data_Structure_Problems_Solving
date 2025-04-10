class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_pointer=0
        second_pointer=0
        result=[]
        max_len=max(len(firstList),len(secondList))
        while(second_pointer<len(secondList) and first_pointer<len(firstList)):
            interval=[]
            if(firstList[first_pointer][1]>=secondList[second_pointer][0] and firstList[first_pointer][0]<=secondList[second_pointer][1]):
                interval=[max(firstList[first_pointer][0],secondList[second_pointer][0]),min(firstList[first_pointer][1],secondList[second_pointer][1])]
                result.append(interval)
            if(secondList[second_pointer][1]>firstList[first_pointer][1]):
                    first_pointer+=1
            else:
                    second_pointer+=1
        return result
