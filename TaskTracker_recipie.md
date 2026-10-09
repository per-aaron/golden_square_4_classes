# Task Tracker Class Design Recipe

## 1. Describe the Problem

>As a user
>So that I can keep track of my tasks
>I want a program that I can add todo tasks to and see a list of them.

Currently assuming singular list of tasks with short text entry for each item.

>As a user
>So that I can focus on tasks to complete
>I want to mark tasks as complete and have them disappear from the list.

Making it easy for the user to select which task(s) they have completed should be a priority. Assuming completed tasks do not need to be stored.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TaskTracker:
    # User-facing properties:
    #   None

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   Init storage for task list
        pass # No code here yet

    def add(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def show(self):
        # Returns:
        #   A numbered list of incomplete tasks
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet

    def complete(self, task_number):
        # Parameters:
        #   task_number: integer representing the (1-indexed)index of the task to mark complete
        # Returns:
        #   Nothing
        # Side-effects
        #   Removes the task from the self object
        #   Prints the task removed as confirmation
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a task
#this task is stored
"""
tasks = TaskTracker()
tasks.add("Walk the dog")
tasks.tasks # => ["Walk the dog"]

"""
Given multiple tasks
#show provides a numbered list with all the tasks
"""
tasks = TaskTracker()
tasks.add("Walk the dog")
tasks.show() # => "1: Walk the dog"

"""
Given no task
#show raises an exception
"""
tasks = TaskTracker()
tasks.show() # raises an error with the message "No task set."

"""
Given multiple tasks and marking one as complete
#complete removes the selected task and show displays only the remaining tasks
"""
tasks = TaskTracker()
tasks.add("Walk the dog")
tasks.add("Please escort your Companion Cube to the Aperture Science Emergency Intelligence Incinerator.")
tasks.add("Please place the Weighted Storage Cube on the Fifteen Hundred Megawatt Aperture Science Heavy Duty Super-Colliding Super Button.")
tasks.add("Now use the Aperture Science Unstationary Scaffold to reach the chamberlock.")
tasks.complete(3) # => ", Kay!"
tasks.show() # => "1: Walk the dog 2: Please escort your Companion Cube to the Aperture Science Emergency Intelligence Incinerator. 3: "Now use the Aperture Science Unstationary Scaffold to reach the chamberlock."
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
