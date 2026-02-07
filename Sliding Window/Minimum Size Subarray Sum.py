class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf") #kept as infinity 

        for r in range(len(nums)): 
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res) #(r - l + 1) is the size of window 
                total -= nums[l]
                l += 1

        return 0 if res == float("inf") else res