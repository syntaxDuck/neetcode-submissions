class Solution:
    def rob(self, nums: List[int]) -> int:
        iMap = {}

        def dfs(i):
            if i >= len(nums):
                return 0

            if i in iMap:
                return iMap[i]
            
            iMap[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return iMap[i]

        return dfs(0)
