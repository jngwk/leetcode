class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # Create functions to compute boolean expressions: !(), &(), |()
        
        def logicalNot(self, exp):
            if exp == 't':
                return 'f'
            return 't'
        def logicalAnd(self, exp):
            print(exp)
            if len(exp) == 1:
                return exp
            arr = exp.split(',')
            if 'f' in arr:
                return 'f'
            return 't'
        def logicalOr(self, exp):
            if len(exp) == 1:
                return exp
            arr = exp.split(',')
            if 't' in arr:
                return 't'
            return 'f'

        openBrackets = []
        # Put brackets into a sequence
        length = len(expression)
        i = 0
        while i != length:
            if expression[i] == '(':
                openBrackets.append({f'{expression[i-1]}' : i})
            elif expression[i] == ')':
                bracket = openBrackets.pop()
                if '|' in bracket:
                    expStart = expression[:bracket.get('|')-1]
                    expEnd = expression[i+1:]
                    expression = expStart + logicalOr(self, expression[bracket.get('|')+1:i]) + expEnd
                    i = bracket.get('|')-2
                elif '&' in bracket:
                    expStart = expression[:bracket.get('&')-1]
                    expEnd = expression[i+1:]
                    expression = expStart + logicalAnd(self, expression[bracket.get('&')+1:i]) + expEnd
                    i = bracket.get('&')-2
                elif '!' in bracket:
                    expStart = expression[:bracket.get('!')-1]
                    expEnd = expression[i+1:]
                    expression = expStart + logicalNot(self, expression[bracket.get('!')+1:i]) + expEnd
                    i = bracket.get('!')-2
            length = len(expression)
            i += 1
        
        print(expression)
        if expression == 'f':
            return False
        elif expression == 't':
            return True

        

        # Compute each boolean expressions in the correct order

        
