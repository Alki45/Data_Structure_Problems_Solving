class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def backtrack(index: int, path: str, eval_val: int, prev_operand: int):
            if index == len(num):
                if eval_val == target:
                    result.append(path)
                return

            for i in range(index, len(num)):
                # Avoid numbers with leading zeros
                if i != index and num[index] == '0':
                    break

                curr_str = num[index:i+1]
                curr_num = int(curr_str)

                if index == 0:
                    # First number, no operator before it
                    backtrack(i+1, curr_str, curr_num, curr_num)
                else:
                    # Try '+'
                    backtrack(i+1, path + '+' + curr_str, eval_val + curr_num, curr_num)
                    # Try '-'
                    backtrack(i+1, path + '-' + curr_str, eval_val - curr_num, -curr_num)
                    # Try '*'
                    backtrack(i+1, path + '*' + curr_str, eval_val - prev_operand + prev_operand * curr_num, prev_operand * curr_num)

        backtrack(0, '', 0, 0)
        return result