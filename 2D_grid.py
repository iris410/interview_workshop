#link list way to solve this
#time O(n) space O(1)
# Grid =>
# R R D
# R U D
# R R L

#0 based indexing =>
# Start(0,0) tuple
# End(2,2) tuple
# is it possible

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
        #O(1)
        direction = {
        "R":(0,1),
        "L":(0,-1),
        "U":(-1,0),
        "D":(1,0)
        }
        cell = grid[i][j]
        dx,dy = direction[cell]
        return(i+dx,j+dy)

    def isPossiblePath(self,grid,start_point,end_point)->bool:
        s = set() # time o(1)
        row = len(grid)
        col = len(grid[0])
        index_a,index_b = start_point
        index_a1,index_b1 = start_point#fast pointer
        target = end_point[0]*col+end_point[1]
        
        number = index_a * col + index_b
        if (number == target):
            return True
#        if(index_a == end_point[0] and index_b==end_point[1]):
#            return True
        
        while(index_a1 < row and index_a1 >= 0 and index_b1 < col and index_b1 >= 0):
            number = index_a * col + index_b
            number2 = index_a1 * col + index_b1

            if number != number2 or (index_a == start_point[0] and index_b ==start_point[1]):
                index_a,index_b = self.updateMove(grid,index_a,index_b)
                index_a1,index_b1 = self.updateMove(grid,index_a1,index_b1)
                number2 = index_a1 * col + index_b1
                if not(index_a1 < row and index_a1 >= 0 and index_b1 < col and index_b1 >= 0):
                    return False
                if(number2 == target):
                    return True
#                if(index_a1 == end_point[0] and index_b1 == end_point[1]):
#                    return True
                index_a1,index_b1 = self.updateMove(grid,index_a1,index_b1)
                number2 = index_a1 * col + index_b1
                if(number2 == target):
                    return True
#                if(index_a1 == end_point[0] and index_b1 == end_point[1]):
#                    return True
            else:
                return False
        return False
         


if __name__ == "__main__":
 #      record_grid=[[]for _ in range(col*row)]
       
    unittest.main()

         

