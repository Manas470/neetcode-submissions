class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        arr = []
        count = 0 
        for i in nums:
            if i in arr:
                count += 1
            else:
                arr.append(i)
                
        if count >= 1:
            return True 
        else:
            return False