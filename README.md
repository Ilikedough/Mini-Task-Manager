# Mini-Task-Manager
Mini-Task-Manager is a program for managing tasks, it lets you add, remove, edit tasks, and it also lets you search for a task or filter them by a property.
Each task has properties which are:
**Name**
the name of the task

**Description**
the description of the task

**Owner**
the owner of the task

**Progress**:
the progress of the task it could be one of three:
- TODO
- IN_PROGRESS
- DONE

**Priority**:
how much the task is prioritised over the others:
- Low
- Medium
- High

**Due Date**  
The date when the task should be completed. It uses a datetime object.

It also contains a logger file that returns a logger, whis is used to log successfull operations in the file called "TM.log" and warn the user for invalid actions in the terminal and the file.

### How to use
#### Add
- Create a TaskManager object
- Create a Task object
- Pass it to TaskManager.add()

#### Remove
- Pass task object file to TaskManager.delete()

#### Edit
- Pass the task and a dictionary of properties to update to TaskManager.edit()

#### Search
- Pass the task id to TaskManager.search()

#### Filter
- Pass a dictionary of properties to TaskManager.filter()


### Example
```python
task_manager = TaskManager()

task = Task(
    name="Homework",
    description="Finish math assignment",
    owner="John"
)

task_manager.add(task)
```