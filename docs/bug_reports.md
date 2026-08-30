# Bug Reports

This document contains issues identified while testing the Student Management API.

## BUG-001 - Invalid Email Accepted

**Title:** API accepts an invalid email format

**Severity:** Medium

**Priority:** Medium

**Module:** Create Student

**Endpoint:**
`POST /students`

### Steps to Reproduce

1. Send a POST request to `/students`.
2. Provide an invalid email such as `invalid-email`.
3. Check the API response.

### Expected Result

The API should reject the invalid email and return a validation error.

### Actual Result

The API returned a `422 Unprocessable Entity` response and rejected the request.

### Status

**Closed / Working as Expected**

### Observation

This test confirmed that the API correctly validates the email format.

---

## BUG-002 - Non-Existent Student Update

**Title:** Update request for a non-existent student

**Severity:** Medium

**Priority:** Medium

**Module:** Update Student

**Endpoint:**
`PUT /students/999`

### Steps to Reproduce

1. Send a PUT request for student ID `999`.
2. Provide valid student data.
3. Check the API response.

### Expected Result

The API should return `404 Not Found` because the student does not exist.

### Actual Result

The API returned `404 Not Found`.

### Status

**Closed / Working as Expected**

### Observation

This test confirmed that the API handles requests for non-existent resources correctly.

---

## Bug Testing Summary

The negative test scenarios were used to check how the API handles invalid input and invalid resource IDs.

The tested scenarios behaved as expected, so no unresolved defects were found during the current test run.