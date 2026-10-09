from lib.ToyStore import *
import pytest

def test_create_empty_toy_store():
    toy_store = ToyStore()
    assert toy_store.toys == []

def test_add_toys_to_store():
    toy_store = ToyStore()
    toy_store.add("Millennium Falcon")
    assert toy_store.toys == ["Millennium Falcon"]

def test_see_toys_returns_list_of_all_toys():
    toy_store = ToyStore()
    toy_store.add("Millennium Falcon")
    toy_store.add("DeLorean")
    assert toy_store.see_toys() == ["Millennium Falcon", "DeLorean"]

def test_error_raised_on_non_string_add():
    toy_store = ToyStore()
    with pytest.raises(TypeError) as e:
        toy_store.add(1)
    
    assert str(e.value) == "'toy' must be a string"