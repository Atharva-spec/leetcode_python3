class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create a result list filled with 1s, same size as nums
        res = [1] * (len(nums))
        
        # 1. First Pass (Prefix): Calculate product of all numbers to the LEFT
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix      # Store the product of elements before index i
            prefix *= nums[i]    # Update prefix to include nums[i] for the next step
        
        # 2. Second Pass (Postfix): Multiply by product of all numbers to the RIGHT
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # Loop backwards from the end
            res[i] *= postfix    # Multiply current left-product by the right-product
            postfix *= nums[i]   # Update postfix to include nums[i] for the next step
            
        return res