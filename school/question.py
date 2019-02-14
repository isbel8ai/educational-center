class Question:
    def __init__(self, statement, choices, answer):
        if not isinstance(statement, str) or statement == "":
            raise ValueError()
        self.subject = statement

        for choice in choices:
            if not isinstance(choice, str) or choice == "":
                raise ValueError()
        # choices is a list of strings of each possible choice
        self.choices = choices

        for check in answer:
            if not isinstance(check, bool):
                raise ValueError()
        # answer is a list of boolean with same size of choices indicating if respective choice should be checked
        self.answer = answer
