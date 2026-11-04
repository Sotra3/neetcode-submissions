class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for i in strs:
            array = [0] * 26
            for j in i:
                array[ord(j) - ord('a')] = array[ord(j) - ord('a')] + 1
            hashMap[tuple(array)].append(i)
        return list(hashMap.values())