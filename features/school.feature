# Created by Isbel at 2/14/2019
Feature: Educational Center
  # Enter feature description here

  Background:
    Given initial data is set

  Scenario: Teacher creates a quiz
    Given data to create a quiz
      | statement | choices           | answer                   |
      | Dark ?    | black, white      | True, False              |
      | Prime ?   | 1, 3, 5, 8        | False, True, True, False |
      | Fruit ?   | apple, dog, table | True, False, False       |
    When the teacher add a new quiz
    Then the quantity of quizzes of the teacher should be 1


  Scenario: Teacher assign quiz to student
    Given the quiz index is 0
    And the group index is 0
    And the student index is 0
    And the semester is 1
    When the teacher assign the quiz to the student
    Then the student should have 1 assignment

  Scenario: Student solve an assignment
    Given the group index is 0
    And the student index is 0
    And the assignment index is 0
    And the solution is
    """
    True, False
    False, True, True, False
    True, False, False
    """
    When the student solve the assignment
    Then the solution should be accepted

  Scenario: Teacher grade student on a semester
    Given the group index is 0
    And the student index is 0
    And the semester is 1
    When Teacher grade the student
    Then the student grade should be 100

