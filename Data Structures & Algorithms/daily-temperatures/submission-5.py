# Solution has O(n^2) time complexity, too slow for large large inputs
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
        temp = []
        for i, t in enumerate(temperatures):
            while temp and t > temperatures[temp[-1]]:
                past_index = temp.pop()
                days = i - past_index
                day_stack[past_index] = days
            temp.append(i)
        return day_stack
