class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        in_block_comment = False
        processed_line = ""
        
        for line in source:
            i = 0
            while i < len(line):
                if not in_block_comment:
                    if i + 1 < len(line) and line[i:i+2] == '/*':
                        in_block_comment = True
                        i += 1
                    elif i + 1 < len(line) and line[i:i+2] == '//':
                        break 
                    else:
                        processed_line += line[i]
                else:
                    if i + 1 < len(line) and line[i:i+2] == '*/':
                        in_block_comment = False
                        i += 1
                
                i += 1
            
            if processed_line and not in_block_comment:
                result.append(processed_line)
                processed_line = ""
        
        return result