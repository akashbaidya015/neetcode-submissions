class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ori = "".join(char.lower() for char in s if char.isalnum())
        
        result = ori[::-1]
            
            
        
        
        
        if result == ori:
            return True
        else:
            return False

        