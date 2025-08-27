import assignment

def test_name_type():
    assert isinstance(assignment.name, str)

def test_age_type():
    assert isinstance(assignment.age, int)

def test_numbers_type():
    assert len(assignment.numbers) == 3

def test_is_students():
    assert assignment.is_student is False 
