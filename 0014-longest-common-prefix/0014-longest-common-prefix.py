class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        resul=sorted(strs)
        output=""
        for i in range(len(resul[0])):
            if(resul[0][i]!=resul[-1][i]):
                break
            output+=resul[-1][i]
        return output
        