class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostFrequent=[]
        result=[]
        hashMap={}
        for i in nums:
            hashMap[i]=hashMap.get(i,0)+1;
        mostFrequent=list(hashMap.values())
        mostFrequent.sort(reverse=True)
        for key,v in hashMap.items():
            if hashMap.get(key,0) >= mostFrequent[k-1]:
                result.append(key)
        result.sort(reverse=True)
        return result