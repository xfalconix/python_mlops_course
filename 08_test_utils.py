import pytest

from utils import str_to_bool


#def test_str_to_bool_yes():
#    result = str_to_bool("Yes")
#    assert result is True

#def test_str_to_bool_y():
 #   result = str_to_bool("y")
  #  assert result is True


@pytest.mark.parametrize("value", ["Yes", "y", "True", "true", "1"])
def test_str_to_bool_true_values(value):
    result = str_to_bool(value)
    assert result is True

@pytest.mark.parametrize("value", ["No", "n", "False", "false", "0"])
def test_str_to_bool_false_values(value):
    result = str_to_bool(value)
    assert result is False

#Terminal:
#pytest -v 08_test_utils.py 
