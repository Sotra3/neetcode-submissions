class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash1={}
        hash2={}
        left=0
        if len(s1)>len(s2):
            return False
        for i in s1:    
            hash1[i]=hash1.get(i,0)+1
        for i in range(len(s1)):
            hash2[s2[i]]=hash2.get(s2[i],0)+1
        if hash1==hash2:
                return True
        for right in range(len(s1),len(s2)):
            out=s2[left]         
            add=s2[right]   
            hash2[out] -= 1
            if(hash2[out]==0):
                del hash2[out]
            left=left+1
            hash2[add]=hash2.get(add,0)+1
            if hash1==hash2:    
                return True
        return False