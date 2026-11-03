class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        result=[]
        count=0
        for i in nums:
            difference=target-i
            if(hashMap.get(difference) is not None):
                result.append(hashMap.get(difference))
                result.append(count)
                break
            hashMap[i]=count
            count=count+1
        return result