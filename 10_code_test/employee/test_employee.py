import pytest
from employee import Employee


@pytest.fixture
def create_employee():
    """Create an employee for all tests."""
    employee1 = Employee('Jordi', 'Ardura', 5_000)
    return employee1


def test_give_default_raise(create_employee):
    """Test if the default raise works."""
    create_employee.give_raise()
    assert create_employee.annual_salary == 10_000


def test_give_custom_raise(create_employee):
    """Test if a custom raise works."""
    create_employee.give_raise(10_000)
    assert create_employee.annual_salary == 15_000
