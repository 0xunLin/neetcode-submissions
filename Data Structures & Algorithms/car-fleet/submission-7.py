class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        arrival_time_stack = []
        for p, s in cars:
            time = (target - p) / s
            if not arrival_time_stack or time > arrival_time_stack[-1]:
                arrival_time_stack.append(time)
        return len(arrival_time_stack)