class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ori = "".join(char.lower() for char in s if char.isalnum())
        temp = [1] * len(ori)
        for i in range(len(ori)):
            
            temp[len(ori)-1-i] = ori[i]
        
        result = "".join(temp)
        print(result,ori)
        if result == ori:
            return True
        else:
            return False

        