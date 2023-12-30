import pytest

from src.descriptor import Descriptor


@pytest.fixture(name="cls_mock")
def fixture_class():
    class Class:
        descriptor = Descriptor()

        def __init__(self, descriptor):
            self.descriptor = descriptor

    return Class


@pytest.mark.parametrize(
    ('descriptor_value',),
    (
        (-1,),
        (-10,),
        (0,),
        (-100.1,),
    ),
)
def test_descriptor_fail(cls_mock, descriptor_value):

    # Assert
    with pytest.raises(ValueError):
        # Act
        cls_mock(descriptor_value)


@pytest.mark.parametrize(
    ('descriptor_value', 'expected'),
    (
        (1, 1),
        (10, 10),
        (1000.1, 1000.1),
    ),
)
def test_descriptor_success(cls_mock, descriptor_value, expected):

    # Assert
    assert cls_mock(descriptor_value).descriptor == expected
