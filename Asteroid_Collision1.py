class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid< 0 < stack[-1]:
                top=stack[-1]

                if abs(top) < abs(asteroid):
                    stack[-1] = asteroid  
                    asteroid = stack.pop()

                elif abs(top) == abs(asteroid):
                    stack.pop()  
                    break

                else:
                    break
                
            else:
                stack.append(asteroid)
        
        return stack
solution = Solution()
asteroids = [10,2,-5]
print(solution.asteroidCollision(asteroids))