class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area_max = 0
        idx_begin = 0
        idx_end = len(height)-1
        while idx_begin != idx_end:
            area = (idx_end - idx_begin)*min(height[idx_begin],height[idx_end])
            if area_max < area:
                area_max = area
            if height[idx_begin] < height[idx_end]:
                idx_begin = idx_begin +1
            else:
                idx_end = idx_end -1
            print(area)
        return(area_max)
                
        
