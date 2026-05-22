class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap ={}
        for num in  nums:
            freqMap[num]=freqMap.get(num, 0)+1
        bucket = [[] for i in range(len(nums)+1)]
        for num,cnt in freqMap.items():
            bucket[cnt].append(num)
        res =[]
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res



        