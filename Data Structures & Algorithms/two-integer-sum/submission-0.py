class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len (nums)
        i = 0
        j = -1
        arr =[]
        while i < n:
            j = i+1
            while j < n:
                if nums[i]+ nums[j]==target:
                    arr=[i,j]
                    return arr
                else :
                    j =j+1
            i+=1
        return arr

        
        


                


            



        