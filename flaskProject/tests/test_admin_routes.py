from flaskProject import create_app

def test_admin_users_requires_auth():
    app = create_app("testing")
    client = app.test_client()
    response = client.get("/admin/users", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data

def test_delete_user_requires_auth():
    app = create_app("testing")
    client = app.test_client()
    response = client.post("/admin/delete/1", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data