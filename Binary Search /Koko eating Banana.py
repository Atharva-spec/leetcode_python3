class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r ) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k) #what does math.ceil do? it rounds up the result of p/k to the nearest integer, which represents the number of hours needed to eat pile p at speed k

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res