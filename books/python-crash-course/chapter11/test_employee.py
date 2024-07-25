import pytest

from employee import Employee


@pytest.fixture
def employee():
    return Employee("Test", "Employee", salary=1000)


def test_give_default_raise(employee):
    assert employee.salary == 1000
    employee.give_raise()
    assert employee.salary == 6000


def test_give_custom_raise(employee):
    assert employee.salary == 1000
    employee.give_raise(2000)
    assert employee.salary == 3000
