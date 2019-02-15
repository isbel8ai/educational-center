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
    assert not assignment.solve([[True, False]])


def test_solve_when_answer_size_not_match(assignment):
    assert not assignment.solve([[True, False, True], [False, True, True, False], [True, False, False]])


def test_solve_partial_solution(assignment):
    assert assignment.solve([None, [False, True, True, False], [True, False, False]])


def test_solve_blank_solution(assignment):
    assert not assignment.solve([None, None, None])


def test_solve(assignment):
    assert assignment.solve([[True, False], [False, True, True, False], [True, False, False]])


def test_evaluate_when_no_solution(assignment):
    assert not assignment.evaluate()


def test_evaluate_partial_solution(assignment):
    assignment.solve([None, [True, True, True, False], [True, False, False]])
    assert assignment.evaluate() == 6 / 9 * 100


def test_evaluate(assignment):
    assignment.solve([[True, False], [True, True, True, False], [True, False, False]])
    assert assignment.evaluate() == 8 / 9 * 100
