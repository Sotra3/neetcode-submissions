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
        print(hash1,hash2)
        if hash1==hash2:
                return True
        for right in range(len(s1),len(s2)):            
            hash2[s2[left]]=hash2.get(s2[left],0)-1
            if(hash2.get(s2[left])==0):
                hash2.pop(s2[left])
            left=left+1
            hash2[s2[right]]=hash2.get(s2[right],0)+1
            print("Hash2:", hash2)
            if hash1==hash2:    
                return True
        return False