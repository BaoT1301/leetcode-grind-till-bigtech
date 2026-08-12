class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        count = 0

        left = 0
        right = len(people) - 1

        while left <= right:
            sum = people[left] + people[right]
            if sum <= limit:
                count += 1
                left += 1
                right -= 1
            elif sum > limit:
                count += 1
                right -= 1

        return count
