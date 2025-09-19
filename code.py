class Solution:
    def spirallyTraverse(self, mat):
        
        m = len(mat)
        n = len(mat[0])
       # code here
        up = 0
        down = m-1
        left = 0
        right = n - 1
        
        result = []
        
        while (right >= left and down >= up):
            
            for i in range(left,right+1):
                result.append(mat[up][i])
            up += 1    
        
            for i in range(up,down+1):
                result.append(mat[i][right])
            right -= 1
            
            if down >= up:
                for i in range(right,left-1,-1):
                    result.append(mat[down][i])
                down -= 1
            
            if right >= left:
                for i in range(down,up-1,-1):
                    result.append(mat[i][left])
                left += 1
            
        return result
        
        
    