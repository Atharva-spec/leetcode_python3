class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res = set() #window 
        l = 0 #start point  
        
        for r in range(len(nums)):
            if r - l > k:
                res.remove(nums[l])
                l += 1
            if nums[r] in res:
                return True

            res.add(nums[r])

        return False 