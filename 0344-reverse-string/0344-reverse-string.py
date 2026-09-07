class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        low = 0
        high = n-1

        while low < high:
            s[low],s[high] = s[high], s[low]
         
    
            low+=1
            high-=1
        