# Student API QA Automation

A small QA project built to practice REST API testing, test case design, bug reporting, API automation, and continuous integration.

The project contains a simple Student Management REST API built with FastAPI and tested using Pytest, Requests, and Postman.

## Project Objective

The objective of this project is to test the main operations of a student management API and verify that it handles both valid and invalid inputs correctly.

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

I created positive and negative test cases to verify normal and incorrect API behaviour.

### Positive Testing

Examples:

- Get all students successfully
- Get an existing student
- Create a valid student
- Update an existing student
- Delete an existing student

### Negative Testing

Examples:

- Request a student that does not exist
- Create a student with an invalid email
- Create a student with an invalid age
- Update a student that does not exist
- Delete a student that does not exist

## Automated Testing

The automated tests are written using **Pytest** and **Requests**.

The test suite verifies:

- HTTP status codes
- Response data
- Input validation
- Error handling
- Non-existent resource handling
- Response time

### Current Test Cases

The project contains 10 automated test cases covering:

1. Get all students
2. Get an existing student
3. Get a non-existent student
4. Create a valid student
5. Create a student with an invalid email
6. Create a student with an invalid age
7. Update an existing student
8. Update a non-existent student
9. Delete a non-existent student
10. Verify API response time

## Postman Testing

The same API was manually tested using **Postman**.

The Postman collection contains requests for:

- GET operations
- POST operations
- PUT operations
- DELETE operations
- Valid test scenarios
- Invalid test scenarios

Postman tests were added to verify:

- HTTP status codes
- Response structure
- Response time

## Test Documentation

The `docs` folder contains:

- `requirements.md` - API requirements and expected behaviour
- `test_cases.md` - Designed test cases and scenarios
- `bug_reports.md` - Documented defects and observations

## Continuous Integration

GitHub Actions is configured to automatically run the Pytest test suite when changes are pushed to the `main` branch or when a pull request is created.

### CI Pipeline

The pipeline:

1. Checks out the project
2. Sets up Python
3. Installs project dependencies
4. Starts the FastAPI application
5. Runs the automated tests

This helps detect test failures automatically after code changes.

## Project Structure

```text
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
```
## How to Run
1. Clone the Repository
git clone https://github.com/kartiksrivastava33-source/student-api-qa.git
cd student-api-qa
2. Create a Virtual Environment
python -m venv .venv
3. Activate the Virtual Environment

On Windows PowerShell:

.venv\Scripts\Activate.ps1
4. Install Dependencies
pip install -r requirements.txt
5. Start the FastAPI Application
uvicorn app:app --reload

The API will start at:

http://127.0.0.1:8000

FastAPI's interactive API documentation is available at:

http://127.0.0.1:8000/docs
6. Run Automated Tests

Open a second terminal in the project directory, activate the virtual environment, and run:

pytest -v

The API must be running in the first terminal while the tests are executed.

7. Generate an HTML Test Report

Run:

pytest --html=reports/test_report.html --self-contained-html

The generated HTML report provides a detailed summary of the test execution.

8. Run Postman Tests

Open Postman and import/open the collection located in:

postman/collections/

Start the FastAPI application first:

uvicorn app:app --reload

Then execute the requests from the Postman collection.

The collection contains both valid and invalid API scenarios.

## Test Results

The current automated test suite contains 10 test cases.

All 10 tests passed successfully:

================ 10 passed in 0.28s ================

## Result Summary
Result	Count
Total Tests	10
Passed	10
Failed	0
Skipped	0

The generated HTML test report also confirms:

10 tests passed
0 tests failed
0 tests skipped
0 unexpected errors
## Test Report

An HTML report was generated using pytest-html:

reports/test_report.html

The report provides information about the test environment, individual test cases, execution time, and overall results.

## Conclusion

This project demonstrates a complete REST API QA testing workflow.

It covers:

REST API testing
Positive and negative test case design
API automation using Pytest and Requests
Manual API testing using Postman
Input validation testing
HTTP status code verification
Error handling verification
Response time validation
Test documentation
Bug reporting
HTML test reporting
Git and GitHub
Continuous integration using GitHub Actions

The project successfully validates the Student Management API through automated and manual testing approaches.
The final automated test suite contains 10 tests, with all 10 tests passing successfully.
This project demonstrates practical experience in designing, executing, automating, documenting, and continuously validating REST APIs.
