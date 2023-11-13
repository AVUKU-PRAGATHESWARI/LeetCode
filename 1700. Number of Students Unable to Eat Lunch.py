class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        while(sandwiches):
            student = students[0]
            if student == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
            else:
                if sandwiches[0] not in students:
                    return len(students)
                students.append(student)
                students.popleft()
        return len(students)