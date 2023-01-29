class Solution:
    # @param A : string
    # @param B : string
    # @param C : list of strings
    # @return an integer
    def solve(self, A, B, C):
        if A == B:
            return 0
        nearestWords, stemmedWords = dict(), dict()
        wordLen = len(A)
        gsw = lambda w: [(w[0:i] + '*' + w[i + 1:]) for i in range(wordLen)]
        for word in [A, B]:
            stemmedWords[word] = gsw(word)
            for stem in stemmedWords[word]:
                if stem not in nearestWords:
                    nearestWords[stem] = []
                nearestWords[stem].append(word)

        for word in C:
            stemmedWords[word] = gsw(word)
            for stem in stemmedWords[word]:
                if stem not in nearestWords:
                    nearestWords[stem] = []
                nearestWords[stem].append(word)

        nodes = [A]
        visited = set()
        depth = {A: 0}
        curDepth = 1
        while len(nodes) != 0 and B not in depth:
            newNodes = []
            for node in nodes:
                if node in visited:
                    continue
                visited.add(node)
                for stem in stemmedWords[node]:
                    for word in nearestWords[stem]:
                        if word != node and word not in visited:
                            newNodes.append(word)
                            depth[word] = curDepth
            nodes = newNodes
            curDepth += 1
        # print(depth)
        return depth[B] + 1 if B in depth else 0
