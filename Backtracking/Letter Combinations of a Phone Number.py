class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitTOchar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curstat):
            if len(curstat) == len(digits):
                res.append(curstat)
                return

            for c in digitTOchar[digits[i]]: #to map the digits
                backtrack(i + 1, curstat + c)

        if digits:
            backtrack(0, "")
        return res
