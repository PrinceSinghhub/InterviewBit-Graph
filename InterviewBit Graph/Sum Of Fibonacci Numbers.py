class Solution:
    # @param A : integer
    # @return an integer
    def fibsum(self, A):
        fibNum = [1, 1]
        i = 1
        while fibNum[i] < A:
            fibNum.append(fibNum[i] + fibNum[i - 1])
            i += 1
        summa = A
        count = 0
        i = len(fibNum) - 1
        while i >= 0 and summa > 0:
            if fibNum[i] > summa:
                i -= 1
            else:
                summa -= fibNum[i]
                count += 1
        return count




