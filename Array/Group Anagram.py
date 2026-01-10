class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #empty list dictionary 
        for s in strs:
            #sorting all the characters alphabetically 
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s) 
        return list(res.values())