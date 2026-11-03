class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1={}
        set2={}
        if len(s)!=len(t) :
            return False
        for i in s:
            set1[i]=set1.get(i,0)+1
        for j in t:
            set2[j]=set2.get(j,0)+1
        for k,v in set1.items():
            if set2.get(k)!=v:
                return False
        return True
