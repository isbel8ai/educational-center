import pytest

from school.question import Question
from school.student import Student


@pytest.fixture
def new_student():
    return Student("Peter Pan")


@pytest.fixture
def student_with_assignments(new_student):
    new_student.add_assignment(
        [
            Question("Dark ?", ["black", "white"], [True, False]),
            Question("Prime ?", ["1", "3", "5", "8"], [False, True, True, False]),
            Question("Fruit ?", ["apple", "dog", "table"], [True, False, False])
        ],
        1
    )
    new_student.add_assignment(
        [
            Question("Planet ?", ["Pluto", "Mars"], [False, True]),
            Question("Even ?", ["1", "3", "5", "8"], [False, False, False, True]),
        ],
        1
    )
    return new_student


@pytest.fixture
def responsible_student(student_with_assignments):
    student_with_assignments.solve_assignment(0, [[True, False], [True, True, True, False], [True, False, False]])
    student_with_assignments.solve_assignment(1, [[True, True], [False, False, False, True]])
    return student_with_assignments


def test_add_assignment(new_student):
    new_student.add_assignment(
        [
            Question("Planet ?", ["Pluto", "Mars"], [False, True]),
            Question("Even ?", ["1", "3", "5", "8"], [False, False, False, True]),
        ],
        1
    )
    assert len(new_student.assignments) == 1


def test_solve_assignment_idx_out_of_range(student_with_assignments):
    with pytest.raises(IndexError):
        student_with_assignments.solve_assignment(4, [[False, True], [False, False, False, True]])


def test_solve_assignment(student_with_assignments):
    student_with_assignments.solve_assignment(1, [[False, True], [False, False, False, True]])


def test_grade_no_assignments_on_semester(responsible_student):
    assert responsible_student.grade(2) == 0


def test_grade(responsible_student):
    assert responsible_student.grade(1) == (8 / 9 + 5 / 6) * 100 / 2
