class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i , j = 0, len(nums) - 0

        while i < j:
            if nums[i] == nums[j]:
                nums(i - j) <= k
                i += 1
                j -= 1
                return True 
            else:
                return False 