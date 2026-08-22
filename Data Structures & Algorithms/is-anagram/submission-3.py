class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_s = {}
        hash_t = {}

        for e in s:
            if e in hash_s:
                hash_s[e] += 1
            else:
                hash_s[e] = 1
        
        for e in t:
            if e in hash_t:
                hash_t[e] += 1
            else:
                hash_t[e] = 1

        return hash_s == hash_t