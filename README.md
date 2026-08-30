# Student API QA Automation

A small QA project built to practice REST API testing, test case design,
bug reporting, API automation, and continuous integration.

The project contains a simple Student Management REST API built with
FastAPI and tested using Pytest, Requests, and Postman.

## Project Objective

The objective of this project is to test the main operations of a student
management API and verify that it handles both valid and invalid inputs correctly.

The API was tested for:

- GET requests
- POST requests
- PUT requests
- DELETE requests
- Invalid input validation
- Non-existent student handling
- Response time

## Tools Used

- Python
- FastAPI
- Pytest
- Requests
- Postman
- Git & GitHub
- GitHub Actions

## API Endpoints Tested

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/students` | Get all students |
| GET | `/students/{id}` | Get a specific student |
| POST | `/students` | Create a student |
| PUT | `/students/{id}` | Update a student |
| DELETE | `/students/{id}` | Delete a student |

## Testing Approach

I created positive and negative test cases to check normal and
incorrect API behaviour.

### Positive testing

Examples:

- Get all students successfully
- Get an existing student
- Create a valid student
- Update an existing student
- Delete an existing student

### Negative testing

Examples:

- Request a student that does not exist
- Create a student with an invalid email
- Create a student with an invalid age
- Update a student that does not exist
- Delete a student that does not exist

## Automated Tests

The automated tests are written using Pytest and Requests.

##Current test suite:

```text
The tests verify HTTP status codes, response data, validation behaviour,
error handling, and response time.

##Postman Testing

The same API was manually tested using Postman.

##The Postman collection contains requests for:

GET operations
POST operations
PUT operations
DELETE operations
Valid and invalid test scenarios

Postman tests were also added to verify status codes, response structure,
and response time.

##Test Documentation

The docs folder contains:

requirements.md - API requirements and expected behaviour
test_cases.md - designed test cases
bug_reports.md - documented defects and observations
Continuous Integration

GitHub Actions is configured to automatically run the Pytest test suite
when changes are pushed to the main branch.

##The CI pipeline:

Checks out the project
Sets up Python
Installs dependencies
Starts the FastAPI application
Runs the automated tests

This helps detect failures after code changes.

##Project Structure
student-api-qa/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── docs/
│   ├── bug_reports.md
│   ├── requirements.md
│   └── test_cases.md
│
├── postman/
│   └── collections/
│
├── tests/
│   └── test_students.py
│
├── app.py
├── pytest.ini
├── requirements.txt
└── README.md
##How to Run

Create and activate a virtual environment:

python -m venv .venv

Install dependencies:

pip install -r requirements.txt

Start the API:

uvicorn app:app --reload

Run the tests in another terminal:

pytest -v

Generate an HTML test report:

pytest --html=reports/test_report.html --self-contained-html
##Result

The current automated test suite contains 10 test cases and all 10
tests pass successfully.
10 tests
10 passed
0 failed
