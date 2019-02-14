from assignment import Assignment


class Student:
    def __init__(self, fullname):
        self.fullname = fullname
        self.assignments = []

    def add_assignment(self, quiz, semester):
        """
        Creates and add a new assignment to student assignments list
        :param quiz: list of questions to be answered
        :param semester: period when quiz is assigned
        """
        assignment = Assignment(quiz, semester)
        self.assignments.append(assignment)

    def solve_assignment(self, assignment_idx, solution):
        """

        :param assignment_idx:
        :param solution:
        """
        if assignment_idx < len(self.assignments):
            self.assignments[assignment_idx].solve(solution)
        else:
            raise IndexError()

    def grade(self, semester):
        """
        Grades student by calculating average of assignments evaluations on specific semester
        :param semester: period when quiz is assigned
        :return: student grade
        """

        count = 0
        total = 0.0
        for assign in self.assignments:
            if assign.semester == semester:
                count += 1
                total += assign.evaluate()

        if count == 0:
            return 0

        return total / count
