class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res ={}
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] +=1
            keyy = tuple(count)
            if keyy not in res:
                res[keyy] = []
            res[keyy].append(s)
        return list(res.values())
        



        