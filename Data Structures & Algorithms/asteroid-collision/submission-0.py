class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            isAlive = True

            while stack and stack[-1] > 0 and a < 0:
                diff = stack[-1] + a

                if diff > 0:
                    isAlive = False
                    break
                elif diff == 0:
                    stack.pop()
                    isAlive = False
                    break
                elif diff < 0:
                    stack.pop()
                    continue
            if isAlive:
                stack.append(a)
            
                    
        return stack
