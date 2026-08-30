# Student Management API - Test Cases

| Test ID | Test Scenario | Method | Endpoint | Expected Result |
|---|---|---|---|---|
| TC-001 | Get all students | GET | /students | 200 |
| TC-002 | Get existing student | GET | /students/1 | 200 |
| TC-003 | Get non-existing student | GET | /students/999 | 404 |
| TC-004 | Create student with valid data | POST | /students | 201 |
| TC-005 | Create student with invalid email | POST | /students | 422 |
| TC-006 | Create student without required field | POST | /students | 422 |
| TC-007 | Update existing student | PUT | /students/1 | 200 |
| TC-008 | Update non-existing student | PUT | /students/999 | 404 |
| TC-009 | Delete existing student | DELETE | /students/1 | 200 |
| TC-010 | Delete non-existing student | DELETE | /students/999 | 404 |
| TC-011 | Check response time | GET | /students | < 2 seconds |