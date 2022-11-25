# Description of the project

The ALX AirBnB project is a test of all we have been doing for the past couple of months now at the ALX Software Engineering Program. The goal of the project is to deploy a replica of the [Airbnb website](https://www.airbnb.com/) on a server. The final version of this project will include:

- A command interpreter to manipulate data like a shell.
- A website(Frontend) with static and dynamic functionalities.
- A database to manage the backend functionalities.
- An API that communicates the backend with the frontend of the whole project.


## General Concepts of the project

At the end of the project, we should have been able to learn the following: 

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- what is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Files and Directories

- `models` directory will contain all classes used for the entre project. A class called "model" in an OOP project is the representation of an object/instance.
- `tests` directory will contain all unit tests files.
- `console.py` file is the entry point of out command interpreter.
- `models/base_model.py` file is the base clas  of all models. It contains elements like
	- attributes: `id`, `created_at`, and `updated_at`.
	- methodes: `save()` and `to_json()`.
- `models/engine`file will contain all storage classes(using the same prototype). At the moment, we will only have one file: `file_storage.py`.

The implementation of the project will happen in the following phases:

## Phase One
This phase is to manipulate a powerful storage system to give an abstraction between objects and how they are stored and persisted. To achieve this, we will:
- put in a parent class ( called BaseModel) to take care of the initialization, serialization and seserialization of future instances
- create a simple flow of serialization/deserializatio: instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB(User, State, City, Place, Review...) that inherits from BaseModel
- create the first abstracted storage engine of the project: File Storage
- create all unittests to validate all our classess and storage engine
- create a data model 
- manage(create, update, destory, etc) objects via a console/command interpreter
- store and persist objects to files(JSON files)S

## Description of the command interpreter
 Commands               	| Descriptions
 -----------------------	|:----------------
 `quit`		       		| Quits the Console
 'Ctrl+D`              		| Quits the console
`help` or `help <command>` 	| Displays all commands or Displays 						   instructions for a specific command
`create <class>`		| Creates an object of type, saves it to a 					  JSON file, and prints the objects ID
`show <class> <ID>`	        | Shows string representation of an object
`destroy <class> <ID>`		| Deletes an object
`all or all <class>`		| Prints all string representation of all objects or 				        prints all string representations of all objects 				    of a specific class
`update <class> <id> <attribute name> "<attribute value>"`  | Updates an object with a 								   certain attribute(new or 								  existing)
`<class>.all()`			| Same as all `<class>`
`<class>.count()`		| Retrieves the number of objects of a certain class
`<class>.show(<ID>)`		| Same as show `<class> <ID>`
`<class>.destroy(<ID>)`		| Same as destroy `<class> <ID>`
`<class>.update(<ID>), <attribute name>, <attribute value>`      | Same as update 								     `<class> <ID> 								       <attribute name> 								    <attribute 								             value>`
`<class>.update(<ID>, <dictionary representation>)`            | Updates an object 							          based on a dictionary 				                                representation of 				                                  attribute name and 						                      values

## General Execution
The shell should work like this ininteractive mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
## Authors
Richard Oluwadamilola

Fiifi Asare-Kumi
