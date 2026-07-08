class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            s = nums[i]
            need = target -s
            if need in nums and nums.index(need)!=i:
                return sorted([i , nums.index(need)])