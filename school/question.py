class Question:
    def __init__(self, statement, choices, answer):
        self.subject = statement
        # choices is a list of strings of each possible choice
        self.choices = choices
        # answer is a list of boolean with same size of choices indicating if respective choice should be checked
        self.answer = answer
