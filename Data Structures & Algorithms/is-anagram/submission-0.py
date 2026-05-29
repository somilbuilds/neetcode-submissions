class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False 
        freq={}
        for car in s:
            if car not in freq:
                freq[car]=1
            else:
                freq[car]+=1
        for char in t:
            if char in freq and freq[char]!=0:
                freq[char]-=1
            else:
                return False
        for chars in freq:
            if freq[chars]!=0:
                return False
        return True

