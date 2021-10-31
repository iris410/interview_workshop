import unittest
class grid_test(unittest.TestCase):
    def test_move(self):
#        self.assertEqual(1+1,2)
#        self.assertEqual(1+1,3)
        self.assertEqual(self.updateMove(self.grid,0,0),(0,1))
        self.assertEqual(self.updateMove(self.grid,2,0),(2,1))
        self.assertEqual(self.updateMove(self.grid,1,1),(1,0))
        return
        
    def test_isPossible(self):
        self.assertEqual(self.isPossiblePath(self.grid,(0,0),(1,2)),True)
        self.assertEqual(self.isPossiblePath(self.grid,(0,2),(1,1)),False)
        self.assertEqual(self.isPossiblePath(self.grid,(0,2),(2,2)),True)
        a = self.grid[0][2]
        self.grid[0][2] = 'R'
        self.assertEqual(self.isPossiblePath(self.grid,(0,2),(2,2)),False)
        self.grid[0][2] = a
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.grid = [
                    ['R','R','D'],
                    ['D','L','D'],
                    ['R','U','U'],
                    ]

    def updateMove(self,grid,i,j):
        cell = grid[i][j]
        if cell == "R":
            j += 1
            return (i,j)
        elif cell == "D":
            i += 1
            return (i,j)
        elif cell == "L":
            j -= 1
            return (i,j)
        else:
            i -= 1
            return (i,j)

    def isPossiblePath(self,grid,start_point,end_point)->bool:
        row = len(grid)
        col = len(grid[0])
        record_grid=[[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                record_grid[i][j] = 0

        index_a,index_b = start_point
        while(index_a < row and index_a >= 0 and index_b < col and index_b >= 0):
            if(record_grid[index_a][index_b] == 0):
                record_grid[index_a][index_b] = 1
                index_a,index_b = self.updateMove(grid,index_a,index_b)
                if(index_a == end_point[0] and index_b == end_point[1]):
                    return True
                
            
            else:
                return False
            
        return False
        



if __name__ == "__main__":
#      record_grid=[[]for _ in range(col*row)]
      
    unittest.main()

        
