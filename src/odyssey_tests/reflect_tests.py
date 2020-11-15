from odyssey.reflect import is_callable

def free_function():
    pass

class empty_class():
    pass

class example_class():
    def __init__(self):
        pass

    def __call__(self):
        pass
    
    def member_function(self):
        pass

example_object = example_class()

def test_is_callable():
    assert is_callable(int)
    assert is_callable(str)
    assert is_callable(list)
    assert not is_callable(1)
    assert not is_callable("dragons")
    assert not is_callable(["hello", "world"])
    assert is_callable(free_function)
    assert not is_callable(free_function())
    assert is_callable(empty_class)
    assert is_callable(example_class)
    assert is_callable(example_class())
    assert is_callable(example_class.member_function)
    assert is_callable(example_class().member_function)
    assert is_callable(example_object)