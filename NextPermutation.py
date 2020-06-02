class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        result = []
        idx = len(nums)-1
        found = False
        
        for i in range(idx, -1, -1):
            print(i)
            if nums[i]>nums[i-1]:
                found = True
                idx_mid = i-1
                break
            
        
        if found == True:
            swap_idx = 0
            min_diff = 0
            for i in range(idx_mid+1,len(nums)):
                print(i,idx_mid,nums[i]-nums[idx_mid])
                if nums[i]-nums[idx_mid] >0 and min_diff == 0:
                    print(nums[i]-nums[idx_mid])
                    min_diff = nums[i]-nums[idx_mid]
                    swap_idx = i
                elif nums[i]-nums[idx_mid] < min_diff and nums[i]-nums[idx_mid] >0 :
                    min_diff = nums[i]-nums[idx_mid]
                    swap_idx = i
            print(swap_idx, min_diff,idx_mid)
            nums[swap_idx], nums[idx_mid] = nums[idx_mid], nums[swap_idx]
            temp = nums[idx_mid+1:]
            temp.reverse()
            print(temp,nums[idx_mid+1:], nums[:idx_mid+1],nums,swap_idx)
            result = nums[:idx_mid+1] +temp
            print(result)
            print("return",result)
            return result
        else:
            result = nums.reverse()
            print("hjgj")
            return result

s = Solution()
res = s.nextPermutation([1,3,2])
print(res)
