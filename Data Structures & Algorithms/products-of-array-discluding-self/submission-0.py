class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        length = len(nums)

        postfix = [1] * length
        pre_pro = 1
        post_pro = 1
        res = []

        # Your exact first loop to build prefix and postfix lists
        for i in range(length):
            pre_pro *= nums[i]
            temp = length - 1 - i
            post_pro *= nums[temp]
            prefix.append(pre_pro)
            postfix[temp] = post_pro

        # Fixed final loop with bounds handling
        for i in range(length):
            left = prefix[i - 1] if i > 0 else 1
            right = postfix[i + 1] if i < length - 1 else 1
            res.append(left * right)

        return res