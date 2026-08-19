class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = list()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                result = nums[i] + nums[j]
                if result == target:
                    output.append(i)
                    output.append(j)
                    return output
                    


        