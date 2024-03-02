class Ll:
    def __init__(self, val: int):
        self.val = val
        self.next = None      

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stdSt = stdEnd = Ll(-1)    # dummy
        food_stack = []
         
        for i in range(0, len(students)):
            stdEnd.next = Ll(students[i])
            stdEnd = stdEnd.next
            food_stack.append(sandwiches[len(sandwiches) - 1 - i])    # Nice trick

        # stdEnd & sandSt pointer is at the end

        counter = 0         # This is the trick to end the loop

        while counter < len(food_stack) :
            if stdSt.next.val != food_stack[-1]:
                stdEnd.next = stdSt.next
                stdEnd = stdEnd.next
                stdSt.next = stdSt.next.next if stdSt.next.next else None
                counter += 1
            else:
                stdSt.next = stdSt.next.next
                food_stack.pop()
                counter = 0
        return counter


