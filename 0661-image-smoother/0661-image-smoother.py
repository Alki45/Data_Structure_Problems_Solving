class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = img[i-1][j-1] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                a = max(0, i - 1)
                b = max(0, j - 1)
                c = min(m - 1, i + 1)
                d = min(n - 1, j + 1)
                s = P[c+1][d+1] - P[a][d+1] - P[c+1][b] + P[a][b]
                res[i][j] = s // ((c - a + 1) * (d - b + 1))
        return res