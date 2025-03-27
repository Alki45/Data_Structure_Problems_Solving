class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        indx = 0  

        while indx < n:
            if arr[indx] == 0: 
                for j in range(n - 1, indx, -1):
                    arr[j] = arr[j - 1]  
                

                if indx + 1 < n:
                    arr[indx + 1] = 0
                
                indx += 1  
            indx += 1 
            
            


        