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
        """
        if len(solution) != len(self.quiz):
            raise ValueError()

        for i, question in enumerate(self.quiz):
            if len(solution[i]) != len(self.quiz[i].answer):
                raise ValueError()

        self.solution = solution

    def evaluate(self):
        """
        Evaluates the solution base on accuracy at choice level and return accuracy percent
        :return: solution accuracy percent
        """
        if self.solution is None:
            raise ValueError()

        total_choices = 0.0
        correct_choices = 0.0

        for i, question in enumerate(self.quiz):
            for j, choice in enumerate(self.quiz[i].answer):
                total_choices += 1
                if self.solution[i][j] == choice:
                    correct_choices += 1

        return correct_choices / total_choices * 100.0
