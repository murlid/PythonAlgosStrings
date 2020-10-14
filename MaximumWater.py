/*
  Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines 
  are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
  Find two lines, which, together with the x-axis forms a container,
  such that the container contains the most water.

  Time complexity O(N) single pass  where N is number of vertical data points
  Space complexity is constant
  
  appeared in Google explorer of LC
  
*/

def maxArea(self, height: List[int]) -> int:

    result, p1, p2 = 0, 0, len(height)-1

    while p1 < p2:
        result = max(result, (p2 - p1)*min(height[p1], height[p2]))
        if height[p1] > height[p2]: p2 -= 1
        else: p1 += 1

    return result
