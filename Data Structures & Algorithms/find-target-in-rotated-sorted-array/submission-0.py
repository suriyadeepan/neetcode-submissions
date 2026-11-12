class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] == target: return l
            if nums[r] == target: return r

            # calculate mid
            mid = (l + r)//2
            if target == nums[mid]: return mid

            # are we in the left sorted portion?
            if nums[l] <= nums[mid]: # yes
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: # no! right sorted portion
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1