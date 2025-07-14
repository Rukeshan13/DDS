class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        t_sum = sum(nums[:])
        for n, ele in enumerate(nums):
            if left == t_sum - left - ele:
                return n
            left += ele
        return -1


        
