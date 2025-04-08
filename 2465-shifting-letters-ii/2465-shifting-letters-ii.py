class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:  # forward
                diff[start] += 1
                diff[end + 1] -= 1
            else:  # backward
                diff[start] -= 1
                diff[end + 1] += 1

        # Apply prefix sum to compute the net shift at each index
        for i in range(1, n):
            diff[i] += diff[i - 1]

        # Apply the shift to the original string
        res = []
        for i in range(n):
            shift = (ord(s[i]) - ord('a') + diff[i]) % 26
            res.append(chr(ord('a') + shift))

        return ''.join(res)