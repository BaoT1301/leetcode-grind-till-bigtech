class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1
        count = 0

        while left <= right:
            weight = people[left] + people[right]

            if weight <= limit:
                count += 1
                left += 1
                right -= 1
            elif weight > limit:
                count += 1
                right -= 1

        return count

