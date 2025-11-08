from app.m.fn import hello

def test_hello1():
    assert hello("me") == "Hello Me!"


def test_hello2():
    assert hello("world") == "Hello World!"