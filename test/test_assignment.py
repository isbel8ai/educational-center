import pytest

from school.assignment import Assignment
from school.question import Question


@pytest.fixture
def assignment():
    quiz = [
        Question("Dark ?", ["black", "white"], [True, False]),
        Question("Prime ?", ["1", "3", "5", "8"], [False, True, True, False]),
        Question("Fruit ?", ["apple", "dog", "table"], [True, False, False])
    ]
    return Assignment(quiz, 1)


def test_solve_when_solution_size_not_match(assignment):
    with pytest.raises(ValueError):
        assignment.solve([[True, False]])


def test_solve_when_answer_size_not_match(assignment):
    with pytest.raises(ValueError):
        assignment.solve([[True, False, True], [False, True, True, False], [True, False, False]])


def test_solve(assignment):
    assignment.solve([[True, False], [False, True, True, False], [True, False, False]])


def test_evaluate_when_no_solution(assignment):
    with pytest.raises(ValueError):
        assignment.evaluate()


def test_evaluate(assignment):
    assignment.solve([[True, False], [True, True, True, False], [True, False, False]])
    assert assignment.evaluate() == 8 / 9 * 100
