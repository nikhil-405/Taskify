# Taskify


## Video Demonstration:
https://youtu.be/pregSUOXgWE


### Installation
* Installing the required Python modules(all the pip-installable modules are also mentioned in the requirements.txt file, and this can be found in the same directory as project.py)

> pip install tabulate

> pip install pandas

> pip install pytest


### Usage
You can use "python {filename}" to run the project

> python project.py

Attached in the same directory as 'project.py' is a file named 'test_project.py', that contains the unit tests for the project.py. The unit tests file can be executed using the below command.

> pytest test_project.py


### Functionality
This is a simple Command Line Interface(CLI) to-do list app. Minimize distractions and get it all done!!

The app has following functionalities:
* You can add tasks to the to-do list
* You can view tasks in your to-do list
* You can update the existing tasks in your to-do list
* You can export your to-do list to a CSV
* You can maintain the status of every task on the to-do list

Every task in the to-do list has following attributes: an integer task ID, the main task itself, and the status of task(C: Completed, In: Incomplete)

When you view the tasks on the list, the output is in a tabular form, presented using Python's tabulate module.


### Design choices
One of the biggest debate with respect to design choices was how to make the app recursively give the user choices to of what task they would like to perform? I ended up using a recursive function call that asks the user if they want to continue or not. Another option for the same was to recursively call the "call" function but that does not give the user enough time to view their tasks (a potential solution for the same is to use the sleep function from Python's time module), but the first option seemed to be more user-friendly and gives more control to the user.


### Future scopes
* We can add user authentication to the app, and make it suitable to be used by multiple accounts

* Instead of simply using arrays to track the record, we can integrate the app to a SQL database, this would allow us to better handle any queries, and even allow us to add additional functionalities for the user(I was unable to figure out how to use an SQL database using mysql-connector, in the codespace)

* We can add in more functionalities such as end-dates/due-dates or reminders, task description, progress made on the task and/or allowing users to have multiple accounts

* Instead of asking the user to recursively enter an integer for their choice, we can use "keylogging-like" route to allow the user to enter
