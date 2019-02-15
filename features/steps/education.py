from behave import *

from school.student import Student
from school.teacher import Teacher

use_step_matcher("re")


@given("initial data is set")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    groups = [
        [Student("Peter Pan"), Student("Wendy Jones"), Student("Marian Pope")],
        [Student("Karina Lin"), Student("Louis Kellen"), Student("John Reno"), Student("George Lima")],
        [Student("Marina Cooks"), Student("Ronald Dooms")]
    ]
    context.teacher = Teacher("Mark Twain", groups)


@given("data to create a quiz")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.statements = []
    context.choices_sets = []
    context.answers = []
    for row in context.table:
        context.statements.append(row['statement'])
        context.choices_sets.append(row['choices'].replace(" ", "").split(","))
        context.answers.append([bool(value) for value in row['answer'].replace(" ", "").split(",")])


@when("the teacher add a new quiz")
@step("the teacher add a new quiz")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.teacher.create_quiz(context.statements, context.choices_sets, context.answers)


@then("the quantity of quizzes of the teacher should be 1")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert len(context.teacher.quizzes) == 1


@given("the quiz index is 0")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.quiz_idx = 0


@step("the group index is 0 and the student index is 0")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.group_idx = 0
    context.student_idx = 0


@step("the semester is 1")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.semester = 1


@when("the teacher assign the quiz to the student")
@step("the teacher assign the quiz to the student")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.teacher.assign_quiz(context.quiz_idx, context.group_idx, context.student_idx, context.semester)


@then("the student should have 1 assignment")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert len(context.teacher.groups[context.group_idx][context.student_idx].assignments) == 1


@step("the assignment index is 0")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.assignment_idx = 0


@step("the solution is")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    solution = []
    for line in context.text.split("\n"):
        if line == "":
            solution.append(None)
        else:
            answer = []
            for value in line.replace(" ", "").split(","):
                answer.append(bool(value))
            solution.append(answer)
    context.solution = solution


@when("the student solve the assignment")
@step("the student solve the assignment")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.solution_accepted = context.teacher.groups[context.group_idx][context.student_idx].solve_assignment(
        context.assignment_idx, context.solution)


@then("the solution should be accepted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.solution_accepted


@when("Teacher grade the student")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.student_grade = context.teacher.grade_student(context.group_idx, context.student_idx, context.semester)


@then("the student grade should be 100")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.student_grade == 100
