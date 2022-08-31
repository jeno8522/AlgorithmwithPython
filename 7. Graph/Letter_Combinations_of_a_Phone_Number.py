from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path): #재귀호출을 위해 index 필요 (뒤로가면서 index 갱신해야하니까)
            if len(path) == len(digits):
                result.append(path)
                return
            for i in range(index, len(digits)): #재귀에서 i, j for문은 단지 전체를 돌리기 위해서지 재귀호출때 사용되는 거랑 다름 (return 문에서 빠져나오므로)
                for j in phone_number[digits[i]]:
                    dfs(i + 1, path + j)

        if not digits:
            return []
        phone_number = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []
        dfs(0,"")

        return result

a = Solution()
print(a.letterCombinations("234"))

