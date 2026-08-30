# Bug Reports

## BUG-001 — API accepts invalid student age

**Status:** Open

**Severity:** Medium

**Priority:** Medium

### Related Requirement

FR-03 / Validation Requirements

Student age must be between 18 and 30.

### Steps to Reproduce

1. Open the Student Management API.
2. Send a POST request to `/students`.
3. Provide age as `15`.
4. Submit the request.

### Test Data

```json
{
  "name": "Test Student",
  "age": 15,
  "email": "test@example.com",
  "course": "ECE"
}

##Expected Result

The API should reject the request with:

422 Validation Error

##Actual Result

The API accepts the request and returns:

201 Created

##Impact

Invalid student records can be created with an age below the allowed range.

### Retest

The API was updated to enforce the student age range of 18–30.

The original test was executed again using age `15`.

**Expected:** 422 Validation Error

**Actual:** 422 Validation Error

**Retest Result:** PASS

### Status

Closed