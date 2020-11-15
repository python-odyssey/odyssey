import pytest
from odyssey.reflect import is_callable, NotCallableError, is_callable_without_class_info, is_method_with_bound_self

def free_function():
    pass

class EmptyClass():
    pass

class ExampleClass():
    def __init__(self):
        pass

    def __call__(self):
        pass
    
    def member_function(self):
        pass

example_object = ExampleClass()

example_lambda = lambda param: param

def test_is_callable():
    assert is_callable(int)
    assert is_callable(str)
    assert is_callable(list)
    assert not is_callable(1)
    assert not is_callable("dragons")
    assert not is_callable(["hello", "world"])
    assert is_callable(free_function)
    assert not is_callable(free_function())
    assert is_callable(EmptyClass)
    assert is_callable(ExampleClass)
    assert is_callable(ExampleClass())
    assert is_callable(ExampleClass.member_function)
    assert is_callable(ExampleClass().member_function)
    assert is_callable(example_object)
    assert is_callable(example_lambda)

def test_is_method_with_bound_self():
    assert not is_method_with_bound_self(int)
    assert not is_method_with_bound_self(str)
    assert not is_method_with_bound_self(list)
    assert not is_method_with_bound_self(free_function)
    assert not is_method_with_bound_self(EmptyClass)
    assert not is_method_with_bound_self(ExampleClass)
    assert not is_method_with_bound_self(ExampleClass())
    assert not is_method_with_bound_self(ExampleClass.member_function)
    assert is_method_with_bound_self(ExampleClass().member_function)
    assert not is_method_with_bound_self(example_object)
    assert is_method_with_bound_self(example_object.member_function)
    assert not is_method_with_bound_self(example_lambda)
