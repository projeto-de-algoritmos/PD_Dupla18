class Solution:
    def climbStairs(self, n: int) -> int:
        S = []
        S = [0] * (n + 1)
        if n == 1:
            return 1
        # Se o numero de passos for 0 entao tera 0 caminhos diferentes 
        S[0] = 0
        
        # Se apenas um passo, tera apenas um caminho
        S[1] = 1

        # Se dois passos, tem dois caminhos
        S[2] = 2
        if n == 2:
            return S[2]
            
        for i in range(3, n+1):
            # Tem dois diferentes caminhos para chegar no kgésimo passo
            # pegue um passo do (k-1)gésimo passo
            # pegue dois passos do (k-2)gésimo passo
            S[i] = S[i-1] + S[i-2]
        # Retorna os diferentes caminhos
        return S[n]