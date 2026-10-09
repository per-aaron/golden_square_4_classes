import pytest
from lib.TaskTracker import *

"""
Given a task
#this task is stored
"""
def test_task_tracker_stores_task():
    tasks = TaskTracker()
    tasks.add("Walk the dog")
    assert tasks.tasks == ["Walk the dog"]

"""
Given multiple tasks
#show provides a numbered list with all the tasks
"""
def test_task_tracker_can_list_multiple_tasks():
    tasks = TaskTracker()
    tasks.add("Walk the dog")
    tasks.add("Make lunch")
    tasks.add("Have a nap")
    assert tasks.show() == [(1, "Walk the dog"), (2, "Make lunch"), (3, "Have a nap")]

"""
Given no task
#show raises an exception
"""
def test_add_raises_error_on_empty_task():
    tasks = TaskTracker()
    with pytest.raises(Exception) as e:
        tasks.show() # raises an error with the message "No task set."
    assert str(e.value) == "No task set."
"""
Given multiple tasks and marking one as complete
#complete removes the selected task and show displays only the remaining tasks
"""
def test_complete_removes_task_from_list():
    tasks = TaskTracker()
    tasks.add("Walk the dog")
    tasks.add("Please escort your Companion Cube to the Aperture Science Emergency Intelligence Incinerator.")
    tasks.add("Please place the Weighted Storage Cube on the Fifteen Hundred Megawatt Aperture Science Heavy Duty Super-Colliding Super Button.")
    tasks.add("Now use the Aperture Science Unstationary Scaffold to reach the chamberlock.")
    tasks.complete(3)
    assert tasks.show() ==  [(1, "Walk the dog"), (2, "Please escort your Companion Cube to the Aperture Science Emergency Intelligence Incinerator."), (3, "Now use the Aperture Science Unstationary Scaffold to reach the chamberlock.")]
