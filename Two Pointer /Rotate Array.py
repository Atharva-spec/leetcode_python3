class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n #ensures k is never larger than the list size
        l, r = 0, len(nums) - 1 #normal rotation of array
        while l < r:
            nums[l], nums[r] = nums[r], nums[l] #helps in rotating an array 
            l,  r = l+1, r - 1

        l, r = 0, k - 1 #from index 0 to k - 1 index
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l,  r = l+1, r - 1
        
        l, r = k, len(nums) - 1 #remaining part of the array 
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l,  r = l+1, r - 1

'''working  
eg: a[1,2,3,4] k[2]
pass 1 : a[4,3,2,1]
pass 2 : a[3,4,2,1]
pass 3 : a[3,4,1,2]
end'''