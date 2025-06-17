from flaskProject import create_app

def test_homepage_loads():
    app = create_app("testing")
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data or b"Welcome" in response.data

def test_login_page_loads():
    app = create_app("testing")
    client = app.test_client()
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data

def test_register_page_loads():
    app = create_app("testing")
    client = app.test_client()
    response = client.get("/register")
    assert response.status_code == 200
    assert b"Register" in response.data

def test_logout_redirects():
    app = create_app("testing")
    client = app.test_client()
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data or b"Home" in response.data

def test_profile_requires_login():
    app = create_app("testing")
    client = app.test_client()
    response = client.get("/profile", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data

def test_edit_profile_requires_login():
    app = create_app("testing")
    client = app.test_client()
    response = client.get("/edit-profile", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data

def test_admin_page_requires_login():
    app = create_app("testing")
    client = app.test_client()
    response = client.get("/admin/users", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data

def test_student_survey_requires_login():
    app = create_app("testing")
    client = app.test_client()
    response = client.get("/survey/student", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data

def test_teacher_survey_requires_login():
    app = create_app("testing")
    client = app.test_client()
    response = client.get("/survey/teacher", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data

def test_find_mentor_requires_login():
    app = create_app("testing")
    client = app.test_client()
    response = client.get("/survey/find-mentor", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data
