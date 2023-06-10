class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        arr=[]
        for i in range(len(queries)):
            a=0
            for j in range(len(points)):
                
                x=points[j][0]
                y=points[j][1]
                eq=(x-queries[i][0])**2+(y-queries[i][1])**2-(queries[i][2])**2
                if eq<=0:
                    a+=1
            arr.append(a)
        return arr
                    
        