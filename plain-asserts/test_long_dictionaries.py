
def test_long_dictionaries():
    results = {"key": "value", "lastname": "Smith", "firstname": "John"}
    expected = {"key": "value", "lastame": "Smith", "firstname": "John"}
    assert results == expected

