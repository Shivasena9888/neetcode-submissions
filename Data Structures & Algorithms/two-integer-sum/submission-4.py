class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap ={}
        for i in range(len(nums)):
            num = nums[i]
            nmap[num] = i
        for i in range(len(nums)):
            num2 = target-nums[i]
            if num2 in nmap and nmap[num2] != i:
                return [i, nmap[num2]]
        
        