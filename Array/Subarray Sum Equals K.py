class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        curSum = 0
        prefixSum = { 0 : 1} #hashmap 

        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefixSum.get(diff,0) #(diff , 0) if there is no difference we will save 0 in our hashmap
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

        return res