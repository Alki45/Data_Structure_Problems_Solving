class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dict_brac = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for char in s:
            if char in dict_brac: 
                stack.append(char)
            else:  
                if stack and dict_brac[stack[-1]] == char:  
                    stack.pop() 
                else:
                    return False 
        if(len(stack)==0):
            return True  
        return False