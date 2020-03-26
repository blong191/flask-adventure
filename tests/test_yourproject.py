import flaskr

def test_import():
    assert flaskr

@pytest.fixture
def app:
    app = create_app({ "TESTING": True })
    yield app
