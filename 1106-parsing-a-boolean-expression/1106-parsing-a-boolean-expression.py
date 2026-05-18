class Solution(object):

    def parseBoolExpr(self, expression):

        self.i = 0

        def solve():

            ch = expression[self.i]

            # true
            if ch == 't':
                self.i += 1
                return True

            # false
            if ch == 'f':
                self.i += 1
                return False

            # operator
            op = ch

            self.i += 2   # skip operator and '('

            values = []

            while expression[self.i] != ')':

                if expression[self.i] == ',':
                    self.i += 1
                    continue

                values.append(solve())

            self.i += 1   # skip ')'

            if op == '!':
                return not values[0]

            elif op == '&':
                return all(values)

            else:
                return any(values)

        return solve()