import pytest

from src.action import Action

def test_abstract_action():
    # Act and Assert
    with pytest.raises(TypeError):
        Action()
