class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        o=0
        for i in range(len(seats)):
            o+=abs(seats[i]-students[i])
        return o
