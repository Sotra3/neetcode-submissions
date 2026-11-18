class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters=set()
        left=0
        result=0
        for right in range(len(s)):
            if s[right] in letters:
                while s[right] in letters:
                    letters.remove(s[left])
                    left=left+1
            letters.add(s[right])
            result=max(result,len(letters))
        return result