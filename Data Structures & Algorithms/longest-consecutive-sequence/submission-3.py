class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        list1 = []
        nums.sort()
        count = 1
        for i in range(len(nums)-1):
            
            if nums[i+1] - nums[i] == 1:
                count += 1
            elif nums[i+1] - nums[i] == 0:
                continue 
            else:
                list1.append(count)
                count = 1
        
        list1.append(count) 
        list1.sort(reverse=True)
        return list1.pop(0)


            


        