class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        list2 = []
        list1 = [[] for _ in range(len(nums) + 1) ]
        for key in nums:
            count[key] = count.get(key,0) + 1
        for key,value in count.items():
            list1[value].append(key)
        for i in range(len(list1)-1,0,-1):
            for num in list1[i]:
                list2.append(num)
                if k == len(list2):
                    return list2



            
        
            

        
            
            
