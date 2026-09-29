class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1
        boat = 0

        while left <= right:
            sum = people[left] + people[right]
            if sum <= limit:
                left += 1
                right -= 1
                boat += 1
            else:
                right -= 1
                boat += 1
        return boat
            