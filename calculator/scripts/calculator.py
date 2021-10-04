class CalculateFromExpression:
    """
    This class calculates result from expressions

    """

    def __init__(self):
        """
        """
        self.__signs = ['+', '-', '*', '/', ')']
        self.__signs_ = ['+', '-', '*', '/', ')', '(']

    def calculate(self, expression):
        """
        Time    O(n) -- linear time
        Space   O(n) -- linear space
        """
        array = []
        for value in expression:
            array.append(value)
        return self.__helper_function(array)

    def __helper_function(self, array):
        if len(array) == 0:
            return 0
        stack = []
        sign = '+'
        number = 0
        while len(array) > 0:
            current_value = array.pop(0)
            if current_value.isdigit():
                number = number * 10 + int(current_value)
            if current_value == '(':
                # do recursion to calculate the sum within the next (...)
                number = self.__helper_function(array)
            if len(array) == 0 or current_value in self.__signs:
                if sign == '+':
                    stack.append(number)
                elif sign == '-':
                    stack.append(-number)
                elif sign == '*':
                    stack[-1] = stack[-1] * number
                elif sign == '/':
                    stack[-1] = float(stack[-1] / float(number))
                sign = current_value
                number = 0
                if sign == ')':
                    break
            if not current_value.isdigit() and current_value not in self.__signs_:
                return 'please give a valid expression'
        return sum(stack)
