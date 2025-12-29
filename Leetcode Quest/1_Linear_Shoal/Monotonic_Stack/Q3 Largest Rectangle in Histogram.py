'''
Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        max_area = 0
        n = len(heights)

        for i in range(n):
            while st and heights[st[-1]]>heights[i]:
                element = st.pop()
                nse = i
                pse = st[-1] if st else -1
                max_area = max(max_area,heights[element] *(nse-pse-1))
            st.append(i)
        while st:
            nse = n
            element = st.pop()
            pse = st[-1] if st else -1
            max_area = max(max_area,heights[element] *(nse-pse-1))
        return max_area
            