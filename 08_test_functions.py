
def str_to_int(string):
    
    error_message = f"Cannot convert '{string}' to an integer."
    try:
        integer = float(string.replace(",", "."))
    except AttributeError:
        if isinstance(string, (int, float)):
            integer = string
        else:
            raise RuntimeError(error_message)
    except (TypeError, ValueError):
        raise RuntimeError(error_message)
    
    return int(integer)

# Test floats

def test_round_down():
    result = str_to_int("3.14")
    assert result == 3

def test_round_down_lesser_half():
    result = str_to_int("3.49")
    assert result == 3


        