class Solution:
    def trap(self, height: List[int]) -> int:
        result=0
        leftMax:List[int]=[]
        rightMax:List[int]=[0]*len(height)
        maximum=0
        for i in range(len(height)):
            if maximum<height[i]:
                maximum=height[i]
            leftMax.append(maximum)

        maximum=0    
        for i in range(1,len(height)+1):
            if maximum<height[-i]:
                maximum=height[-i]  
            rightMax[-i]=maximum

        for i in range(len(height)):
            result+=min(leftMax[i],rightMax[i])-height[i]  
        return result