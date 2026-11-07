class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum=1
        result:List[int]=[]
        nulls=0
        for i in nums:
            if i!=0:
                sum*=i
            else:
                nulls+=1
        for i in nums:
            if nulls>1:
                result.append(0)
            elif i==0 and nulls==1:
                result.append(sum)
            elif i!=0 and nulls==1:
                result.append(0)
            else:
                result.append(sum//i)
        return result