class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        r = 1
        if x == 0:
            return 0
        while n > 0:
            if n & 1:
                r = self.mul_mod(r, x, d)
            n = n >> 1
            x = self.mul_mod(x, x, d)
        return r
    def mul_mod(self, a, b, m):
        a %= m
        b %= m
        r = (a * b) % m
        return r