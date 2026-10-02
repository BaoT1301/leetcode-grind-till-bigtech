class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        stack = []

        cars.sort(reverse=True)

        for pos, spd in cars:
            time_to_target = (target - pos) / spd

            if not stack:
                stack.append(time_to_target)
            elif time_to_target > stack[-1]:
                stack.append(time_to_target)

        return len(stack)

