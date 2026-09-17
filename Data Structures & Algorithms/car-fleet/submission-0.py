class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for pos, spd in cars:
            arrival_time = (target - pos) / spd

            if not stack or arrival_time > stack[-1]:
                stack.append(arrival_time)
        return len(stack)
