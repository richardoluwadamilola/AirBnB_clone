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
- `models/base_model.py file is the base clas  of all models. It contains elements like
	- attributes: `id`, `created_at`, and `updated_at`.
	- methodes: save() and to_json().
 
