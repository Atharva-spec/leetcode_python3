class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            #m = (l + r) // 2 if the input array is v large mgiht face overflow
            m = l + ((r - l) // 2) #this wont overflow
            if nums[m] > target:
                r = m - 1 #the right half would not have the target in it so we shift the r pointer
            elif nums[m] < target:
                l = m + 1 #same logic for left pointer
            else:
                return m
        return -1