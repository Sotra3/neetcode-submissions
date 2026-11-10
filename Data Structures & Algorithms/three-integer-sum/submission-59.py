class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        result:List[List[int]]=[]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue          
            front = i + 1
            back = len(nums) - 1
            while front < back:
                s = nums[i] + nums[front] + nums[back]
                if s > 0:
                    back -= 1
                elif s < 0:
                    front += 1
                else:
                    result.append([nums[i], nums[front], nums[back]])
                    front += 1
                    while front < back and nums[front] == nums[front - 1]:
                        front += 1 
        return result