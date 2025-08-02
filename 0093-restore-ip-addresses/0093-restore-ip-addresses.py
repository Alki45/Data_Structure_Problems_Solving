class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def is_valid(segment: str) -> bool:
            return len(segment) == 1 or (segment[0] != '0' and int(segment) <= 255)

        def backtrack(start: int, path: List[str]):
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return

            for end in range(start + 1, min(start + 4, len(s) + 1)):
                segment = s[start:end]
                if is_valid(segment):
                    backtrack(end, path + [segment])

        backtrack(0, [])
        return result