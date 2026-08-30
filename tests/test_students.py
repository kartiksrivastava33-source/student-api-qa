import requests


BASE_URL = "http://127.0.0.1:8000"


def test_get_all_students():
    response = requests.get(f"{BASE_URL}/students")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_existing_student():
    response = requests.get(f"{BASE_URL}/students/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "name" in data
    assert "email" in data
    assert "course" in data


def test_get_nonexistent_student():
    response = requests.get(f"{BASE_URL}/students/999")

    assert response.status_code == 404


def test_create_student():
    student = {
        "name": "Test Student",
        "age": 21,
        "email": "test@example.com",
        "course": "CSE"
    }

    response = requests.post(
        f"{BASE_URL}/students",
        json=student
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Test Student"
    assert data["age"] == 21
    assert data["email"] == "test@example.com"


def test_create_student_invalid_email():
    student = {
        "name": "Test Student",
        "age": 21,
        "email": "invalid-email",
        "course": "CSE"
    }

    response = requests.post(
        f"{BASE_URL}/students",
        json=student
    )

    assert response.status_code == 422


def test_create_student_invalid_age():
    student = {
        "name": "Test Student",
        "age": 15,
        "email": "test@example.com",
        "course": "CSE"
    }

    response = requests.post(
        f"{BASE_URL}/students",
        json=student
    )

    assert response.status_code == 422


def test_update_student():
    student = {
        "name": "Updated Student",
        "age": 22,
        "email": "updated@example.com",
        "course": "ECE"
    }

    response = requests.put(
        f"{BASE_URL}/students/1",
        json=student
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Updated Student"
    assert data["age"] == 22


def test_update_nonexistent_student():
    student = {
        "name": "Updated Student",
        "age": 22,
        "email": "updated@example.com",
        "course": "ECE"
    }

    response = requests.put(
        f"{BASE_URL}/students/999",
        json=student
    )

    assert response.status_code == 404


def test_delete_nonexistent_student():
    response = requests.delete(f"{BASE_URL}/students/999")

    assert response.status_code == 404


def test_response_time():
    response = requests.get(f"{BASE_URL}/students")

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2