class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        output = 0
        n = len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                smallest = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                output = max(output, heights[smallest] * width)
            stack.append(i)
        while stack:
            smallest = stack.pop()
            width = n if not stack else n - stack[-1] -1
            output = max(output, heights[smallest] * width)
        return output