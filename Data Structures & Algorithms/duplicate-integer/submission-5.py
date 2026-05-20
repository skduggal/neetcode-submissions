class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()

        n = len(nums)

        for i in range(n):
            while n > 1:
                if nums[i] == nums[i - 1]:
                    return True
                break
                
        return False


        
