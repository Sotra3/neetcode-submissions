class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers=set()
        current=0
        maximum=0
        for i in nums:
            numbers.add(i)
        for n in numbers:
            current=0
            if n-1 not in numbers:
                while n in numbers:
                    current=current+1
                    n=n+1
                maximum=max(current,maximum)
        return maximum