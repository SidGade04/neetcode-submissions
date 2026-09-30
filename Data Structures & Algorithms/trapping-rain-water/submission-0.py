class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        maxArea = 0

        while left < right:
            if (height[left] > height[right]):
                right -= 1
                rightMax = max(rightMax, height[right])
                maxArea += rightMax - height[right]
            else:
                left += 1
                leftMax = max(leftMax, height[left])
                maxArea += leftMax - height[left]

        return maxArea