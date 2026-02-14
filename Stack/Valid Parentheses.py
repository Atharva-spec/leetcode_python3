class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        closetoopen = {")":"(", "}":"{", "]":"["} #hashtable note the brackets should be facing opposite eachother instead of towards 

        for i in s:
            if i in closetoopen:
                if res and res[-1] == closetoopen[i]:
                    res.pop()
                else:
                    return False
            else:
                res.append(i)

        return True if not res else False             
