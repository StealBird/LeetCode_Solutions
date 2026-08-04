class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        ans = [0] *(m+n)
        left = 0
        right = 0
        index = 0

        while(left<m and right<n):
            if nums1[left] <= nums2[right]:
                ans[index] = nums1[left]
                left += 1
                index += 1
            else:
                ans[index] = nums2[right]
                right += 1
                index += 1
        while (left<m):
            ans[index] = nums1[left]
            left += 1
            index += 1

        while (right<n):
            ans[index] = nums2[right]
            right += 1
            index += 1

        for i in range(0, n+m):                 
            nums1[i] = ans[i]
            
            
        
        
        