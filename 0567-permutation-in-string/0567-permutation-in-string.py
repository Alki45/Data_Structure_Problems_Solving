class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1 = Counter(s1)
        count_window = Counter(s2[:len(s1)])
        
        if count_s1 == count_window:
            return True

        for i in range(len(s1), len(s2)):
            start_char = s2[i - len(s1)]
            end_char = s2[i]

            count_window[end_char] += 1
            count_window[start_char] -= 1

            if count_window[start_char] == 0:
                del count_window[start_char]

            if count_window == count_s1:
                return True
        
        return False