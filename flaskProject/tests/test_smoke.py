from flaskProject import create_app

def test_app_starts():
    app = create_app('testing')
    assert app is not None