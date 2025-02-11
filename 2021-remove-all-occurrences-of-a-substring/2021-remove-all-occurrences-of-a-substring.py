
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """ while(part in s):
                s=s.replace(part,' ')
                print(s)
        return s"""

        stack=[]
        len_part=len(part)
        for char in s:
            stack.append(char)
            if len(stack) >= len_part and "".join(stack[-len_part:]) == part:
                del stack[-len_part:]

        return "".join(stack)