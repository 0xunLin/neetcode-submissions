# Solution has O(n^2) time complexity, too slow for very large inputs
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         o = []
#         for i in range(len(temperatures)):
#             for j in range(i+1, len(temperatures)):
#                 if temperatures[j] > temperatures[i]:
#                     o.append(j - i)
#                     break
#             if len(o) < i+1:
#                 o.append(0)
#         return o

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        day_stack = [0] * len(temperatures)
        temp_stack = []
        for i, temp in enumerate(temperatures):
            while temp_stack and temp > temperatures[temp_stack[-1]]:
                top_popped = temp_stack.pop()
                days = i - top_popped
                day_stack[top_popped] = days
            temp_stack.append(i)
        return day_stack

