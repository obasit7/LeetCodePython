from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visitSet, prevHeight):
            if ((r, c)) in visitSet or r >= rows \
                    or c >= cols or heights[r][c] < prevHeight \
                    or r < 0 or c < 0:
                return

            visitSet.add((r, c))
            newPrev = heights[r][c]
            dfs(r, c + 1, visitSet, newPrev)
            dfs(r, c - 1, visitSet, newPrev)
            dfs(r + 1, c, visitSet, newPrev)
            dfs(r - 1, c, visitSet, newPrev)

        for c in range(cols):  # up to down and vise versa
            # 0, c - every col in first row
            dfs(0, c, pacific, heights[0][c])  # next height needs to be equal or greater
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res