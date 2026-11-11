class Solution:
    def trap(self, height: List[int]) -> int:
        
        def dp():
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

        maxL, maxR = 0, 0
        l, r = 0, len(height)-1

        total = 0
        while l < r:
            if height[l] <= height[r]:
                total += max(0, maxL - height[l])
                maxL = max(maxL, height[l])
                l += 1
            else:
                total += max(0, maxR - height[r])
                maxR = max(maxR, height[r])
                r -= 1

        return total






















