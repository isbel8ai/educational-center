import pytest

from school.student import Student
from school.teacher import Teacher


@pytest.fixture
def new_teacher():
    groups = [
        [Student("Peter Pan"), Student("Wendy Jones"), Student("Marian Pope")],
        [Student("Karina Lin"), Student("Louis Kellen"), Student("John Reno"), Student("George Lima")],
        [Student("Marina Cooks"), Student("Ronald Dooms")]
    ]
    return Teacher("Mark Twain", groups)


@pytest.fixture
def teacher_with_quiz(new_teacher):
    statements = ["Dark ?", "Prime ?", "Fruit ?"]
    choices_sets = [["black", "white"], ["1", "3", "5", "8"], ["apple", "dog", "table"]]
    answers = [[True, False], [False, True, True, False], [True, False, False]]
    new_teacher.create_quiz(statements, choices_sets, answers)
    return new_teacher


def test_create_quiz_no_statements(new_teacher):
    statements = []
    choices_sets = [["black", "white"], ["1", "3", "5", "8"], ["apple", "dog", "table"]]
    answers = [[True, False], [False, True, True, False], [True, False, False]]
    assert not new_teacher.create_quiz(statements, choices_sets, answers)
    assert len(new_teacher.quizzes) == 0


def test_create_quiz_choices_diff_size(new_teacher):
    statements = ["Dark ?", "Prime ?", "Fruit ?"]
    choices_sets = [["black", "white"], ["1", "3", "5", "8"]]
    answers = [[True, False], [False, True, True, False], [True, False, False]]
    assert not new_teacher.create_quiz(statements, choices_sets, answers)
    assert len(new_teacher.quizzes) == 0


def test_create_quiz_answers_diff_size(new_teacher):
    statements = ["Dark ?", "Prime ?", "Fruit ?"]
    choices_sets = [["black", "white"], ["1", "3", "5", "8"], ["apple", "dog", "table"]]
    answers = [[True, False], [False, True, True, False]]
    assert not new_teacher.create_quiz(statements, choices_sets, answers)
    assert len(new_teacher.quizzes) == 0


def test_create_quiz(new_teacher):
    statements = ["Dark ?", "Prime ?", "Fruit ?"]
    choices_sets = [["black", "white"], ["1", "3", "5", "8"], ["apple", "dog", "table"]]
    answers = [[True, False], [False, True, True, False], [True, False, False]]
    assert new_teacher.create_quiz(statements, choices_sets, answers)
    assert len(new_teacher.quizzes) == 1


def test_assign_quiz_with_quiz_idx_out_of_range(teacher_with_quiz):
    with pytest.raises(IndexError):
        teacher_with_quiz.assign_quiz(2, 0, 0, 1)


def test_assign_quiz_with_group_idx_out_of_range(teacher_with_quiz):
    with pytest.raises(IndexError):
        teacher_with_quiz.assign_quiz(0, 5, 0, 1)


def test_assign_quiz_with_student_idx_out_of_range(teacher_with_quiz):
    with pytest.raises(IndexError):
        teacher_with_quiz.assign_quiz(0, 0, 8, 1)


def test_assign_quiz(teacher_with_quiz):
    teacher_with_quiz.assign_quiz(0, 0, 0, 1)
