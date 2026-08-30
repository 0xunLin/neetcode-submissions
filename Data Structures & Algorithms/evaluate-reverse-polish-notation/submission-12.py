class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case '+':
                    o1 = stack.pop()
                    o2 = stack.pop()
                    stack.append(o2 + o1)
                case '-':
                    o1 = stack.pop()
                    o2 = stack.pop()
                    stack.append(o2 - o1)
                case '*':
                    o1 = stack.pop()
                    o2 = stack.pop()
                    stack.append(o2 * o1)
                case '/':
                    o1 = stack.pop()
                    o2 = stack.pop()
                    stack.append(int(o2 / o1))
                case val:
                    stack.append(int(val))
        return stack.pop()

# Same solution, typecast where you want to
# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []
#         for token in tokens:
#             match token:
#                 case '+':
#                     o1 = stack.pop()
#                     o2 = stack.pop()
#                     stack.append(o2 + o1)
#                 case '-':
#                     o1 = stack.pop()
#                     o2 = stack.pop()
#                     stack.append(o2 - o1)
#                 case '*':
#                     o1 = stack.pop()
#                     o2 = stack.pop()
#                     stack.append(o2 * o1)
#                 case '/':
#                     o1 = stack.pop()
#                     o2 = stack.pop()
#                     stack.append(int(o2 / o1))
#                 case val :
#                     stack.append(int(val))
#         return int(stack[0])