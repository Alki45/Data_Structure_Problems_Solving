class Solution(object):
    def minimumRecolors(self, blocks, k):
        n = len(blocks)
        min_operations = float('inf')

        for i in range(n - k + 1):
            white_count = 0
 
            for j in range(i, i + k):
                if blocks[j] == 'W':
                    white_count += 1

            min_operations = min(min_operations, white_count)
        
        return min_operations