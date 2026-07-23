class Solution:
    def isPalindrome(self, s):              
        cleaned = self.clean(s)            
        return self.is_palindrome_recursive(cleaned, 0, len(cleaned)-1)

    def clean(self, s):
        copy=""
        for char in s:
            if char.isalnum():
                copy+=char
        copy = copy.lower()
        return copy

    def is_palindrome_recursive(self, s, l, r):   
        if l >= r:
            return True
        if s[l] != s[r]:
            return False
        return self.is_palindrome_recursive(s, l+1 ,r-1)
        