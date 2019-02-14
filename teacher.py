from question import Question


class Teacher:
    def __init__(self, fullname, groups):
        self.fullname = fullname
        # groups is a list containing in each position a list of students (a group)
        self.groups = groups
        # quizzes is a list containing in each position a list of questions (a quiz)
        self.quizzes = []

    def create_quiz(self, statements, choices_sets, answers):
        """
        Creates a quiz by creating the a list of questions
        :param statements:
        :param choices_sets:
        :param answers:
        """
        questions_count = len(statements)

        if questions_count == 0:
            return False

        if len(choices_sets) != questions_count or answers != questions_count:
            return False

        quiz = []
        for i in range(questions_count):
            question = Question(statements[i], choices_sets[i], answers[i])
            quiz.append(question)

        self.quizzes.append(quiz)
        return True

    def assign_quiz(self, quiz_idx, group_idx, student_idx, semester):
        """
        Assigns a quiz to a student for specific semester
        :param quiz_idx:
        :param group_idx:
        :param student_idx:
        :param semester:
        """
        if quiz_idx < len(self.quizzes) and group_idx < len(self.groups) and student_idx < len(self.groups[group_idx]):
            self.groups[group_idx][student_idx].add_assignment(self.quizzes[quiz_idx], semester)
        else:
            raise IndexError()
