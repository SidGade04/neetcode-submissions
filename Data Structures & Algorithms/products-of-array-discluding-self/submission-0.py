class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            nums2 = nums[:i] + nums[i+1:]
            res.append(math.prod(nums2))
        return res