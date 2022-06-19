import numpy as np
class Solution:
    def isHappy(self, n: int) -> bool:
        
        visit = set()

        while n not in visit:
            visit.add(n)

            n = self.sum_ints(n)

            if n == 1:
                return True
        return False
    
    def sum_ints(self, n):
        
        x = [int(a) for a in str(n)]
        x = np.sum(np.dot(x,x))
        return x
