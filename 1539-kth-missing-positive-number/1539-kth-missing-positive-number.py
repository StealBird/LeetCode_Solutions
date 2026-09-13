class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low , high = 0 , len(arr)-1

        while low <= high:
            mid = (low+high)//2
            req = arr[mid] - (mid+1)
            if req < k:
                low = mid+1
            else: #req>=k
                high = mid-1
        return low+k