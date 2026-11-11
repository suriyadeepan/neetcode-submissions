class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        maxLeft = [0] * N 
        maxRight = [0] * N
        total = 0

        for i in range(1, N):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])

        for i in range(N-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i+1])

        for i in range(N):
            minLR = min(maxLeft[i], maxRight[i])
            total += max(0, minLR - height[i])

        return total