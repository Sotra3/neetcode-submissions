class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded:str=""
        for i in strs:
            encoded+=str(len(i))+"#"+i
        return encoded

    def decode(self, s: str) -> List[str]:
        coded:List[str]=[]
        word:str=""
        size_str:str=""
        size_int:int=0
        state:int=0
        for i in s:
            if state!=0:
                word+=i
                size_int-=1
                if size_int==0:
                    coded.append(word)
                    word="" 
                    state=0   
            else:
                if(i.isdigit()==True):
                    size_str+=i
                if i=="#":
                    size_int=int(size_str)
                    size_str=""
                    if size_int == 0:
                        coded.append("")
                    else:
                        state = 1

        return coded