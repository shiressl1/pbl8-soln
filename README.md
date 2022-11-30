# PBL 9: Unit testing

This session is an opportunity to practice creating and running a test case using the Paralympics web app scenario.
There is also an opportunity to see the information that results from using GitHub Actions for continuous integration (automatically running tests when code is committed/pushed to GitHuB) and linting (automatically checking for code
quality using Flake8).

The activities use pytest as the test library, and pytest-cov for coverage.


## Set up

1. Create a copy of the repo using 'User this template' in GitHub.
2. Clone the new repo you just created from your GitHub account to your IDE (VS Code, PyCHarm).
3. Create and activate a venv.
4. Install pytest and pytest-cov e.g., `pip install pytest pytest-cov`.

## Problem 1: Test files and folders

The sample repo has a models.py file that has the classes from the UML class diagram. Some methods have been
implemented.

Please note that the code is rudimentary and is not an example of how the methods will actually be written when we use
Flask and Dash in term 2.

There are some deliberate errors in the code, and no doubt some un-intentional errors too!

1. Create a directory for the tests.
2. In the directory, create an empty Python file in which you will write tests for the classes in `models.py`.
3. In the directory, create a new Python file called `conftest.py`.

**Remember to use appropriate naming conventions.**

## Problem 2: Create a fixture

1. In `conftest.py`, add a fixture that provides data to create a new general public user.

Hints: 

The structure of a fixture:
```python
import pytest

@pytest.fixture(scope='module')
def values():
   values = [2, 4, 8, 20]
   yield values
```

To create a new user import the GeneralPublic class from para_cycle.models and create an instance of the class with values for each of the attributes (username, password, email, phone).
```python
from para_cycle.models import GeneralPublic

gp_user = GeneralPublic(username='uname', password='pass', email='email@email.com', phone='09999 999999')
```


## Problem 3: Create and run a unit test

1. Write Python code in the python test file you created in Problem 1 to create the following test. It should use the
   fixture that you created in Problem 2.

The test has been described using the Given-When-Then model:

```text
GIVEN a new user (created as a fixture)
WHEN it the user has just been created
THEN the logged in status should be False
```

Remember to use a meaningful test name and pass the fixture as a parameter. The following example uses a fixture called 'values' e.g.
```python
def test_minimum_returns_correct_value(values): 
   """
   GIVEN the values 2, 4, 8 and 20
   WHEN the values are passed to the minimum function 
   THEN the result should equal 2
   """
   result = algorithm.minimum(values)
   assert result == 2
```

2. Run the test code with pytest using the verbose parameter. Either use your IDE's interface or the command line.

e.g. to run from the terminal
```
python -m pytest -v
```

## Problem 4: Run a coverage report

1. Run the tests using coverage with the optional parameters and identify which lines are not covered by tests.

The general syntax to run pytest from the terminal with coverage is shown as follows:
```
python -m pytest --cov=project_name
```

The general syntax to run pytest from the terminal with coverage and a more detailed report showing lines not covered by tests is shown as follows:
```
python -m pytest --cov-report term-missing --cov=myproj tests/
```

## Problem 5: Create an additional test

1. Create another test using the Given-When-Then model:

```text
GIVEN a user is logged in
WHEN the logout function is called
THEN the logged in status should be False
```

2. Run the test with coverage.

The general syntax to run pytest from the terminal with coverage and a more detailed report showing lines not covered by tests is:
```
python -m pytest --cov-report term-missing --cov=myproj tests/
```

The test fails, why?

3. Extension: consider the lines of code not currently covered, write another test that improves your coverage.


## Problem 6: Using GitHub Actions

GitHub Actions provides a way to automatically run a defined series of steps (called a 'workflow') that happens on a
given change to your repository.

In this repo a GitHub Actions workflow has already been created that runs the tests and a linter whenever code is
updated in the main/master branch.

Creating a workflow is covered in the teaching materials for this week (see the 'How to..' guide). Creating up a GitHub
workflow for continuous integration is set as a challenge and not covered in the tutorials or PBL. You are strongly
encouraged to consider establishing a GitHub Actions workflow for your coursework.

The purpose of this 'problem' is to use the information available in the workflow to decide what changes you may need to
make to your code.

1. Commit and push your changes to GitHub.
2. Go to the repository on GitHub and find the Actions tab.
3. Under 'All workflows' select the 'Python application' workflow.
4. Click on the most recent workflow run.
5. Clock on 'build'.
6. Expand the section for 'Lint with flake8' and 'Test with pytest and cov' (click on the '>' symbol to expand).
    - What does the information tell you?
    - What actions could you take as a result of this information?
