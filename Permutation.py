class Solution(object):
    def Permutation(self, nums,l):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if l == len(nums)-1:
            print(nums)
        for i in range(l,len(nums)):
            nums[l],nums[i] = nums[i],nums[l]
            self.Permutation(nums,l+1)
            nums[i],nums[l] = nums[l],nums[i]


S = Solution()
S.Permutation([1,3,4,2],0)
