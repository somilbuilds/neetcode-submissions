class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index={}
        for i,w in enumerate(nums):
            if target-w in index:
                return [index[target-w],i]
            else:
                index[w]=i
