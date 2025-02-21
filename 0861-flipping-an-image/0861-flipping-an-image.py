class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i].reverse()
        r=len(image)
        c=len(image[0])
        for row in range(r):
            for col in range(c):
                if(image[row][col]==0):
                    image[row][col]=1
                elif(image[row][col]==1):
                    image[row][col]=0
        return image
                
        