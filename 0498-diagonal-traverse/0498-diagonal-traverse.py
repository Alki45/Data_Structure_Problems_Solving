class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        result=[]
        direction=1
        row,col=0,0
        while (row<m and col<n) :
            result.append(mat[row][col])
            if(direction==1):
                if(col==n-1):
                    row+=1
                    direction=-1
                elif(row==0):
                    col+=1
                    direction=-1
                else:
                    row-=1
                    col+=1
            else:
                if(row==m-1):
                    col+=1
                    direction=1
                elif(col==0):
                    row+=1
                    direction=1
                else:
                    col-=1
                    row+=1
        return result


