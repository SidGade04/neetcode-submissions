class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            left, right = 0, len(m) - 1
            
            while left <= right:
                mid = left + ((right - left) // 2)

                if m[mid] > target:
                    right = mid - 1
                elif m[mid] < target:
                    left = mid + 1
                else:
                    return True
        
        return False