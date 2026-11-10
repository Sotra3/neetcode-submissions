class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums={}
        remaining=0
        index1=0
        index2=0
        for i in range(len(numbers)):
            remaining=target-numbers[i]
            if remaining in nums:
                index1=min(i+1,nums.get(remaining))
                index2=max(i+1,nums.get(remaining))
                break
            else:
                nums[numbers[i]]=i+1
        return [index1,index2]