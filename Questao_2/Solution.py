from pip import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def helper(sum, left, right):
            if len(sum) == n*2:
                res.append(sum)
                return
            if left < n: 
                helper(sum + "(", left + 1, right)
            if left > right: 
                helper(sum + ")", left, right + 1)
        
        helper("", 0, 0)
        return res
    
    #Modifique as entradas aqui
    print(generateParenthesis(1,3))