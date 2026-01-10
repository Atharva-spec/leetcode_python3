class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) #array into a set
        longest = 0

        for num in numSet: #check if its the start of a sequence 
            if (num - 1) not in numSet:
                lenght = 0
                while (num + lenght) in numSet:
                    lenght +=1
                longest = max(lenght, longest)
        return longest 