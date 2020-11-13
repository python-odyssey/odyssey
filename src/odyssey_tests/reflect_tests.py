from odyssey.reflect import is_callable

def free_function():
    pass

def test_is_callable():
    assert is_callable(int)
    assert is_callable(str)
    assert is_callable(list)
    assert not is_callable(1)
    assert not is_callable("dragons")
    assert not is_callable(["hello", "world"])
    assert is_callable(free_function)
    assert not is_callable(free_function())