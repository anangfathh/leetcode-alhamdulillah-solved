class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,-1),(0,1),(-1,0),(1,0)]

        def depth_first_search(x, y, t, visited):
            if x == n-1 and y == n-1:
                return True
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] <= t:
                    if depth_first_search(nx, ny, t, visited):
                        return True
            return False

        low, high, ans = 0, n*n - 1, float('inf')
        while low <= high:
            mid = (low + high) // 2
            visited = [[False]*n for _ in range(n)]
            if grid[0][0] <= mid and depth_first_search(0, 0, mid, visited):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans