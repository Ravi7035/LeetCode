class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]

        mapping={
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for char in s:

            if char in mapping:

                if not stack:

                    return False


                top=stack.pop()

                if top != mapping[char]:

                    return False

            else:

                stack.append(char)
            

        return not stack


                