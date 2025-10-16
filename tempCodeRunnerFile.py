class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        prevPrev, prev = 1, 2
        for _ in range(3, n + 1):
            curr = prevPrev + prev
            prevPrev, prev = prev, curr
        return curr
