class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap={}
        current=0
        maximum=0
        for i in nums:
            hashMap[i]=hashMap.get(i,0)+1

        for k,v in hashMap.items():
            if hashMap.get(k-1,0)==0:
                temp=k
                while(hashMap.get(temp,0)!=0):
                    current=current+1
                    temp=temp+1
                if(current>maximum):
                    maximum=current
                current=0
        return maximum