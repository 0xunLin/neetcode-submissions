class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case '+':
                    o1 = int(stack.pop())
                    o2 = int(stack.pop())
                    stack.append(o2 + o1)
                case '-':
                    o1 = int(stack.pop())
                    o2 = int(stack.pop())
                    stack.append(o2 - o1)
                case '*':
                    o1 = int(stack.pop())
                    o2 = int(stack.pop())
                    stack.append(o2 * o1)
                case '/':
                    o1 = int(stack.pop())
                    o2 = int(stack.pop())
                    stack.append(o2 / o1)
                case val :
                    stack.append(val)
        return int(stack[0])

# Same solution, typecast where youy want to
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