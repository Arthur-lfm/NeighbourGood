# NeighbourGood

NeighbourGood is a web application that allows users to post and find items that they no longer need. Users can post items that they no longer need and other users can claim the items. Users can also search for items that they need and claim them.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installation

1. To use this application, you will need to have Python and Django installed on your machine.
```sh
pip install django
```

2. Once you have installed Django, you can clone this repository:
```sh
git clone https://github.com/Arthur-lfm/NeighbourGood.git
```

3. Change into the directory containing the project and migrate the database:
```sh
cd NeighbourGood
python3 manage.py migrate
```

4. Then, create a superuser account to access the admin panel:
```sh
python3 manage.py createsuperuser
```

5. Finally, run the development server:
```sh
python3 manage.py runserver
```

You can now access the application at http://localhost:8000/polls/ and the admin panel at http://localhost:8000/admin/.

#### Testing methodology and coverage

Testing Methodology
The testing methodology used for this Django application is Test-Driven Development (TDD). TDD is a software development process that involves writing tests for the desired functionality before writing the code to implement that functionality.

The TDD process for this application involved the following steps:

1. Write a failing test for the desired functionality.
2. Write the code to implement the functionality.
3. Run the test and verify that it passes.
4. Refactor the code as necessary to improve its design and maintainability.
5. Repeat the process for additional functionality.

Using TDD ensures that the application meets the desired requirements and prevents regressions from occurring when new features are added or existing features are modified.

Test Coverage
The test coverage for this Django application is 100%. Test coverage is a metric that measures the degree to which the code is tested by the test suite. A coverage report is generated after running the test suite, which shows which lines of code are covered by the tests and which lines are not.

Achieving 100% test coverage means that every line of code in the application is executed at least once during the test suite. This ensures that the code is thoroughly tested and any bugs or regressions are caught before they are introduced into the production environment.

To achieve 100% test coverage, the following types of tests were written:

1. Unit tests: These tests verify the functionality of individual units of code, such as models, forms, and utility functions.
2. Integration tests: These tests verify the interactions between different units of code, such as views and templates.
3. Functional tests: These tests verify the functionality of the application from the user's perspective, such as submitting forms and navigating between pages.
In addition to achieving 100% test coverage, the test suite was also run on multiple platforms and environments to ensure that the application works as expected across different configurations.
