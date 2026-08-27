class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashTable = {}

        for num in nums:
            if num in hashTable:
                return True
            else:
                hashTable[num] = 1
        return False
        