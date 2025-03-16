class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height)-1  #initializing two poiters and creating variable "max_water"
        max_water = 0 
        while left < right:  #repeating array
            #calculating current area
            width = right-left
            min_height = min(height[left],height[right])
            area = width*min_height
            max_water=max(area,max_water)

            if height[left]<height[right]:  # Move the pointer pointing to the shorter height
                left+=1
            else:
                right-=1

        return max_water
