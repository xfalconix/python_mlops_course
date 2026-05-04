
def str_to_bool(val):

    """Convert a string to a boolean.

    Args:
        val (str): The string to convert.

    Returns:
        bool: The converted boolean value.
    """
    true_vals=["true", "1", "t", "y", "yes"]
    false_vals=["false", "0", "f", "n", "no"]
    try:
        val = val.lower()
    except AttributeError as e:
        val=str(val).lower()
    if val in true_vals:
        return True
    elif val in false_vals:
        return False
    
def str_to_int(string):
    #first try to do a float
    result = float (string)
    #then convert to an int and return it
    return int(result)
