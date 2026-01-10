class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i] + nums[j] < target: #becuase the sum is less than target so we add another number 
                i += 1
            elif nums[i] + nums[j] > target: #elif plays a imp role we decrease j because moving forward would just increase the value which of no use for us
                j -= 1
            else:
                nums[i] + nums[j] == target
                break
        return [i+1, j+1]
            