class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        while n:
            for i in range(32):
                res = (res << 1) | (n & 1)
                n = n >> 1         
        return res

