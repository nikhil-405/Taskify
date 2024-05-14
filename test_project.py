# Unit tests for project.py

import pytest
from project import *
# Not the best practice but gets the job done

def test_add():
    data = [[1, 2], ['Groceries', 'Swimming'], ['In.', 'In.']]
    new_data = add(data, "Physics Homework", "In.")
    assert new_data == [[1, 2, 3], ['Groceries', 'Swimming', "Physics Homework"], ['In.', 'In.', 'In.']]

    data = [[], [], []]
    new_data = add(data, "Physics Homework", "In.")
    assert new_data == [[1], ["Physics Homework"], ["In."]]

def test_update():
    data = [[1, 2], ['Groceries', 'Swimming'], ['In.', 'In.']]
    new_data = update(data, 2, "Physics Homework", "C.")
    assert new_data == [[1, 2], ['Groceries', 'Physics Homework'], ['In.', 'C.']]


def test_comp():
    data = [[1, 2], ['Groceries', 'Swimming'], ['In.', 'In.']]
    comp(data, 2)
    assert data == [[1, 2], ['Groceries', 'Swimming'], ['In.', 'C.']]
