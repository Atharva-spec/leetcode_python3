class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # Hashmap to count how often each number appears
        freq = [[] for i in range(len(nums) + 1)] # Create buckets where index = frequency

        for n in nums:
            count[n] = 1 + count.get(n, 0) # Count the frequency of each number

        for n, c in count.items():
            freq[c].append(n) # Group numbers into the bucket matching their count

        res = [] # List to store the final answer
        for i in range(len(freq) - 1, 0, -1): # Loop backwards from highest frequency
            for n in freq[i]:
                res.append(n) # Add the number to our result list
                if len(res) == k:
                    return res # Stop and return once we have k numbers