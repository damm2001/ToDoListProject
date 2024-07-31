Feature: To-Do List Management
  As a user, I want to manage my tasks in a to-do list so that I can keep track of my tasks.

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When I add a task with title "Buy groceries" and description "Buy milk and eggs"
    Then the to-do list should contain a task with title "Buy groceries" and description "Buy milk and eggs"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains the following tasks:
      | Title          | Description         |
      | Buy groceries  | Buy milk and eggs   |
      | Pay bills      | Pay electricity bill|
    When I list all tasks
    Then I should see the following tasks:
      | Title          | Description         |
      | Buy groceries  | Buy milk and eggs   |
      | Pay bills      | Pay electricity bill|

  Scenario: Mark a task as completed
    Given the to-do list contains a task with title "Buy groceries" and description "Buy milk and eggs"
    When I mark the task "Buy groceries" as completed
    Then the task "Buy groceries" should be marked as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks
    When I clear the to-do list
    Then the to-do list should be empty

  Scenario: Delete a task from the to-do list
    Given the to-do list contains a task with title "Buy groceries" and description "Buy milk and eggs"
    When I delete the task "Buy groceries"
    Then the to-do list should not contain a task with title "Buy groceries"

  Scenario: Edit a task in the to-do list
    Given the to-do list contains a task with title "Buy groceries" and description "Buy milk and eggs"
    When I edit the task "Buy groceries" with new title "Buy vegetables" and new description "Buy carrots and potatoes"
    Then the to-do list should contain a task with title "Buy vegetables" and description "Buy carrots and potatoes"
