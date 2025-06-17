from flaskProject import create_app

def test_homepage_loads():
    app = create_app("testing")
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data or b"Welcome" in response.data

def test_profile_requires_login():
    app = create_app("testing")
    client = app.test_client()
    response = client.get("/profile", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data

def test_admin_page_requires_login():
    app = create_app("testing")
    client = app.test_client()
    response = client.get("/admin/users", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data

def test_edit_profile_requires_login():
    app = create_app("testing")
    client = app.test_client()
    response = client.get("/edit-profile", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data
