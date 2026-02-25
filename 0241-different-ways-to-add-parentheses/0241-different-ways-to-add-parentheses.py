class Solution(object):
    def diffWaysToCompute(self, expression):
        def DiffWaysToCompute(expression):
            result=[]
            
            for i in range(len(expression)):

                if expression[i] in "-+*":

                    left=DiffWaysToCompute(expression[:i])
                    right=DiffWaysToCompute(expression[i+1:])

                    for l in left:
                        for r in right:
                            
                            if expression[i]=="+":

                                result.append(l+r)

                            elif expression[i]=="-":

                                result.append(l-r)

                            else:

                                result.append(l*r)

            if not result:
                result.append(int(expression))

            return result


        return DiffWaysToCompute(expression)

        
        