Airbnb Clone README
Project Description
This is a command-line driven Airbnb clone that allows users to create, update, and delete objects. The project is built using Python and utilizes a custom command interpreter to interact with the user.
Command Interpreter
Starting the Interpreter
To start the command interpreter, navigate to the project directory and run the following command:
./console.py

Using the Interpreter
The interpreter supports the following commands:
create <class_name>: Creates a new object of the specified class.
show <class_name> <id>: Displays the details of an object with the specified ID.
destroy <class_name> <id>: Deletes an object with the specified ID.
all: Displays all objects.
update <class_name> <id> <attribute_name> "<attribute_value>": Updates an attribute of an object with the specified ID.
Examples
Create a new User object: create User
Show a User object with ID 123: show User 123
Destroy a User object with ID 123: destroy User 123
Update the email attribute of a User object with ID 123: update User 123 email "new_email@example.com"
