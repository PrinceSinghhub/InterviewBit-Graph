from collections import deque


class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def stepnum(self, A, B):

        queue = deque([i for i in range(10)])
        s = set()
        res = []

        while queue:

            next_num = queue.popleft()
            if A <= next_num <= B and next_num not in s:
                res.append(next_num)
                s.add(next_num)

            if next_num > B:
                continue

            last_digit = next_num % 10
            if last_digit == 0:
                queue.append(next_num * 10 + 1)
            elif last_digit == 9:
                queue.append(next_num * 10 + 8)
            else:
                queue.append(next_num * 10 + last_digit - 1)
                queue.append(next_num * 10 + last_digit + 1)

        return res

