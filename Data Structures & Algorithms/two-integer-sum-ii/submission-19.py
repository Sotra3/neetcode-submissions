class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1=0
        index2=len(numbers)-1
        while(index1<index2):
            s=numbers[index1]+numbers[index2]
            if s==target:
                break
            elif s>target:
                index2-=1
            else:
                index1+=1
        return [index1+1,index2+1]