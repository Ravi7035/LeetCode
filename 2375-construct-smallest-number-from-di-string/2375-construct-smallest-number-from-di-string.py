class Solution(object):
    def smallestNumber(self, pattern):
        """
        n = len(pattern)
        used = [False] * (n + 2)
        answer = []
        def backtrack(path):
            if len(path) == n + 1:
                answer.append("".join(path))
                return True  

            for digit in range(1, n + 2):
                if not used[digit]:
                    
                    if path:
                        prev = int(path[-1])
                        idx = len(path) - 1

                        if pattern[idx] == 'I' and prev >= digit:
                            continue
                        if pattern[idx] == 'D' and prev <= digit:
                            continue

                    used[digit] = True
                    path.append(str(digit))

                    if backtrack(path): 
                        return True

                    path.pop()
                    used[digit] = False

            return False

        backtrack([])
        return answer[0]

        """

        #stack version 
        res=[]
        stack=[]
        num=1

        for char in pattern:
            stack.append(num)
            num+=1
            if char=="I":
                while stack:
                    res.append(stack.pop())

        stack.append(num)

        while stack:
            res.append(stack.pop())

        return "".join(str(digit) for digit in res)


        



