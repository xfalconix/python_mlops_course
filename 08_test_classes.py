
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

class TestStrToInt:

    def setup(self):
        print("\nthis is setup")

    def teardown(self):
        print("\nthis is teardown")
    
    def setup_class(cls):
        print("\nthis is setup_class")
    
    def teardown_class(cls):
        print("\nthis is teardown_class")

    def test_rounds_down(self):
        result = str_to_int("1.99")
        assert result == 2
        