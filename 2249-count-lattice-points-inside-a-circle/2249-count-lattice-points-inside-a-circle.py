class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        
        arr = set()
    
        def point(x, y, r):
            

            for a in range(x-r, x+r+1):
                for b in range(y-r, y+r+1):
                    if (a-x)*(a-x) + (b-y)*(b-y) <= r*r:
                        arr.add((a,b))

            return arr
        
        for x in circles:

            point(x[0],x[1],x[2])

        return len(arr)

        