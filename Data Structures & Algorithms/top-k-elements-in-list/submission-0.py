class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max ={}
        for i in nums :
            if i in max :
                max[i]= max[i]+1
            else :
                max[i]=1
        final = sorted(max.keys(), key = lambda x:max[x], reverse = True)
        return final [:k]




        