class Assignment:
    def __init__(self, quiz, semester):
        self.quiz = quiz
        self.semester = semester
        # solution is a list of answers for each question on the quiz
        self.solution = None

    def solve(self, solution):
        """
        Validates the solution data structure, if it is correct 'solution' is set as assignment solution,
        if not raise ValueError
        :param solution: list of answers for each question on the quiz
        :return True if solution has correct format and False if not
        """
        if solution is None or len(solution) != len(self.quiz):
            return False

        answered = False

        for i, question in enumerate(self.quiz):
            if solution[i] is None:
                continue
            else:
                answered = True
            if len(solution[i]) != len(self.quiz[i].answer):
                return False

        if answered:
            self.solution = solution
            return True
        return False

    def evaluate(self):
        """
        Evaluates the solution base on accuracy at choice level and return accuracy percent
        :return: solution accuracy percent
        """
        if self.solution is None:
            return False

        total_choices = 0.0
        correct_choices = 0.0

        for i, question in enumerate(self.quiz):
            total_choices += len(question.answer)
            if self.solution[i]:
                for j, choice in enumerate(question.answer):
                    correct_choices += float(self.solution[i][j] == choice)

        return correct_choices / total_choices * 100.0
