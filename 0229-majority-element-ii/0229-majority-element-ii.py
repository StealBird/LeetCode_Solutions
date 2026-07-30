class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c1 = 0
        c2 = 0
        e1 = float('-inf')
        e2 = float('-inf')

        for i in range(0,n):
            if c1 == 0 and e2 != nums[i]:
                c1 = 1
                e1 = nums[i]
            elif c2 == 0 and e1 != nums[i]:
                c2 = 1
                e2 = nums[i]
            elif nums[i] == e1:
                c1 += 1
            elif nums[i] == e2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        c1 = 0
        c2 = 0

        for i in range(0, n):
            if nums[i]==e1:
                c1+=1
            if nums[i]==e2:
                c2+=1
        mini = (n//3)+1
        result = []

        if c1>=mini:
           result.append(e1)
        if c2>=mini and e1 != e2:
            result.append(e2)


        result.sort()

        return result