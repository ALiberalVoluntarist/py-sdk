from src.hello import greetings


def test_greetings():
    assert greetings() == 'Hello, World!'
