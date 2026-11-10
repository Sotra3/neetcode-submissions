class Solution:
    def maxArea(self, heights: List[int]) -> int:
        front = 0
        end = len(heights)-1
        best=0
        while(front<end):
            a=heights[front]
            b=heights[end]
            c=end-front
            if(min(a,b)*c>best):
                best=min(a,b)*c
            if(a>b):
                end=end-1
            else:
                front=front+1
        return best
        