import pytest

@pytest.mark.parametrize("HDL_input, expected",
    [(85, "Normal"),
    (45, "Borderline Low"),
    (20, "Low")])
def test_check_HDL(HDL_input, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(HDL_input)
    assert answer == expected

'''
def test_check_HDL_BorderlineLow():
    from blood_calculator import check_HDL
    answer = check_HDL(50)
    expected = "Borderline Low"
    assert answer == expected

def test_check_HDL_High():
    from blood_calculator import check_HDL
    answer = check_HDL(20)
    expected = "Low"
    assert answer == expected
'''