# Student Management API - Requirements

## 1. Overview

The Student Management API is a simple REST API used to manage student records.

Each student contains:

- ID
- Name
- Age
- Email
- Course

## 2. Functional Requirements

### FR-01: Get All Students

The system should allow users to retrieve all students.

**Endpoint:**

GET /students

**Expected response:**

- Status code: 200
- Response should contain a list of students.

---

### FR-02: Get Student by ID

The system should allow users to retrieve a specific student using their ID.

**Endpoint:**

GET /students/{student_id}

**Expected behavior:**

- Existing student → 200
- Non-existing student → 404

---

### FR-03: Create Student

The system should allow users to create a new student.

**Endpoint:**

POST /students

Required fields:

- name
- age
- email
- course

**Expected behavior:**

- Valid data → 201
- Invalid data → 422

---

### FR-04: Update Student

The system should allow users to update an existing student.

**Endpoint:**

PUT /students/{student_id}

**Expected behavior:**

- Existing student → 200
- Non-existing student → 404

---

### FR-05: Delete Student

The system should allow users to delete an existing student.

**Endpoint:**

DELETE /students/{student_id}

**Expected behavior:**

- Existing student → 200
- Non-existing student → 404

---

## 3. Validation Requirements

The API should reject invalid student information.

### Age

- Age must be an integer.
- Age must be between 18 and 30.
- Values below 18 must be rejected.
- Values above 30 must be rejected.

### Email

- Email must have a valid email format.

### Required Fields

The following fields are required:

- name
- age
- email
- course

---

## 4. Non-Functional Requirement

API responses should normally be returned within 2 seconds under normal local testing conditions.