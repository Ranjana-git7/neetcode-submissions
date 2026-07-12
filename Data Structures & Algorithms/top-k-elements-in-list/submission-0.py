class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num , 0)+1

        sorted_count = sorted(count.items() , key =  lambda x: x[1] , reverse = True)
        result = []
        for i in range (k):
            result.append(sorted_count[i][0])
        return result 
       