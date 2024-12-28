class Solution:
    def maxScoreSightseeingPair(self, values):
        res = 0 
        bestPrev = values[0] - 1

        for i in range(1, len(values)):
            res = max(res, values[i] + bestPrev)
            bestPrev = max(bestPrev - 1, values[i] -1 ) # for the next iteration 
        return res
    
if __name__ == "__main__":
    obj = Solution()
    values = [8, 1, 5, 2, 6]
    print(obj.maxScoreSightseeingPair(values))


