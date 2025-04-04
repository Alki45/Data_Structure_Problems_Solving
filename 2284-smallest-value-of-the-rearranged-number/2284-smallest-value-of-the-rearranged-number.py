class Solution:
    def smallestNumber(self, num: int) -> int:
        New_num = ""
        if num >= 0:
            New_num = list(str(num))
            New_num.sort()
            if New_num[0] != '0':
                return int("".join(New_num))
            else:
                for i in range(1, len(New_num)):
                    if New_num[i] != '0':
                        New_num[0], New_num[i] = New_num[i], New_num[0]
                        break
                return int("".join(New_num))
        else:
            New_num = list(str(num))
            Neg = New_num[1:]
            Neg.sort(reverse=True)
            result = [New_num[0]] + Neg
            return int("".join(result))