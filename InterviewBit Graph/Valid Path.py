import math


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def intersect_upper_half(self, i, j, r, x, y):
        if (i <= r):
            return True
        elif (j + r >= y):
            return True
        else:
            return False

    def intersect_lower_half(self, i, j, r, x, y):
        if (i + r >= x):
            return True
        elif (j <= r):
            return True
        else:
            return False

    def circle_intersect(self, i, j, x, y, r):
        distance = math.sqrt((x - i) ** 2 + (y - j) ** 2)
        if (distance <= 2 * r):
            return True
        else:
            return False

    def check_circles(self, i, circles, visited):
        visited[i] = True
        if (self.intersect_lower_half(circles[i][0], circles[i][1], self.r, self.x, self.y)):
            return True
        else:
            for index in range(len(circles)):
                if (not visited[index]):
                    if (
                    self.circle_intersect(circles[i][0], circles[i][1], circles[index][0], circles[index][1], self.r)):
                        ret_var = self.check_circles(index, circles, visited)
                        if (ret_var):
                            return True
            return False

    def solve(self, A, B, C, D, E, F):
        self.x = A
        self.y = B
        n = C
        self.r = D
        circles = [(a, b) for a, b in zip(E, F)]
        for i in range(n):
            if (self.intersect_upper_half(circles[i][0], circles[i][1], self.r, self.x, self.y)):
                ret_var = self.check_circles(i, circles, [False] * n)
                if (ret_var):
                    return "NO"
        return "YES"

