class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNums = set(nums)
        if len(list(setNums) )== len(nums):
            return False
        return True