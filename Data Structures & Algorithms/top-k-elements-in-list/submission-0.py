class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        list1 = []
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0) + 1
        for key,value in count.items():
            list1.append(value)
        list1.sort(reverse=True)
        first = list1[:k]
        list2 = []
        keys = list(count.keys())
        values = list(count.values())
        for i in range(len(first)):
            idx = values.index(list1[i])
            key = keys.pop(idx)
            values.pop(idx)
            list2.append(key)

        return list2
            
            
