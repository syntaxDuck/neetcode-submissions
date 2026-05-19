class Solution:
    def climbStairs(self, n: int) -> int:

        one, two = 1, 1
        for i in range(n - 1):
            one_0 = one
            one = one + two
            two = one_0
        
        return one
        