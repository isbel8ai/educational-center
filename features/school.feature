# Created by Isbel at 2/14/2019
Feature: Educational Center
  # Enter feature description here

  Background:
    Given initial data is set

  Scenario: Teacher creates a quiz
    When teacher 0 add a new quiz
      | statement | choices           | answer                   |
      | What ?    | this, that        | True, False              |
      | Prime ?   | 1, 3, 5, 8        | False, True, True, False |
      | Fruit ?   | apple, dog, table | True, False, False       |
    Then the quantity of quizzer of teacher 0 should be 1


  Scenario: Teacher assign quiz to student
    When teacher 0

