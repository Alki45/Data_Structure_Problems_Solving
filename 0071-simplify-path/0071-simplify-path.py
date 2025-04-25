class Solution:
    def simplifyPath(self, path: str) -> str:
        New_list = path.split('/')
        result = []

        for i in New_list:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if result:
                    result.pop()
            else:
                result.append(i)
        
        final_path = '/' + '/'.join(result)
        
        return final_path