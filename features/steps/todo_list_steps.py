from behave import given, when, then
from main import ToDoListManager

@given('the to-do list is empty')
def step_given_todo_list_empty(context):
    context.manager = ToDoListManager()

@when('I add a task with title "{title}" and description "{description}"')
def step_when_add_task(context, title, description):
    context.manager.add_task(title, description)

@then('the to-do list should contain a task with title "{title}" and description "{description}"')
def step_then_todo_list_contains_task(context, title, description):
    task = next((task for task in context.manager.tasks if task.title == title and task.description == description), None)
    assert task is not None, f'Task with title "{title}" and description "{description}" not found.'

@given('the to-do list contains the following tasks:')
def step_given_todo_list_contains(context):
    context.manager = ToDoListManager()
    for row in context.table:
        context.manager.add_task(row['Title'], row['Description'])

@when('I list all tasks')
def step_when_list_tasks(context):
    pass  # Las tareas ya están en context.manager.tasks, solo se deben verificar en el paso @then

@then('I should see the following tasks:')
def step_then_should_see_tasks(context):
    expected_tasks = [(row['Title'], row['Description']) for row in context.table]
    actual_tasks = [(task.title, task.description) for task in context.manager.tasks]
    assert expected_tasks == actual_tasks, f'Expected tasks: {expected_tasks}, but got: {actual_tasks}'

@given('the to-do list contains a task with title "{title}" and description "{description}"')
def step_given_todo_list_contains_task(context, title, description):
    context.manager = ToDoListManager()
    context.manager.add_task(title, description)

@when('I mark the task "{title}" as completed')
def step_when_mark_task_completed(context, title):
    task_number = next((i for i, task in enumerate(context.manager.tasks, 1) if task.title == title), -1)
    if task_number != -1:
        context.manager.mark_task_as_completed(task_number)

@then('the task "{title}" should be marked as completed')
def step_then_task_should_be_completed(context, title):
    task = next((task for task in context.manager.tasks if task.title == title), None)
    assert task is not None and task.completed, f'Task "{title}" is not marked as completed.'

@given('the to-do list contains tasks')
def step_given_todo_list_contains_tasks(context):
    context.manager = ToDoListManager()
    context.manager.add_task("Task 1", "Description 1")
    context.manager.add_task("Task 2", "Description 2")

@when('I clear the to-do list')
def step_when_clear_todo_list(context):
    context.manager.clear_tasks()

@then('the to-do list should be empty')
def step_then_todo_list_should_be_empty(context):
    assert len(context.manager.tasks) == 0, 'The to-do list is not empty.'

@when('I delete the task "{title}"')
def step_when_delete_task(context, title):
    task_number = next((i for i, task in enumerate(context.manager.tasks, 1) if task.title == title), -1)
    if task_number != -1:
        context.manager.delete_task(task_number)

@then('the to-do list should not contain a task with title "{title}"')
def step_then_task_should_not_be_present(context, title):
    task = next((task for task in context.manager.tasks if task.title == title), None)
    assert task is None, f'Task with title "{title}" is still present in the to-do list.'

@when('I edit the task "{old_title}" with new title "{new_title}" and new description "{new_description}"')
def step_when_edit_task(context, old_title, new_title, new_description):
    task_number = next((i for i, task in enumerate(context.manager.tasks, 1) if task.title == old_title), -1)
    if task_number != -1:
        context.manager.edit_task(task_number, new_title, new_description)
