import pytest

@pytest.mark.parametrize("HDL_input, expected",
    [(85, "Normal"),
    (45, "Borderline Low"),
    (20, "Low")])
def test_check_HDL(HDL_input, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(HDL_input)
    assert answer == expected

@pytest.mark.parametrize("LDL_input, expected",
    [(85, "Normal"),
    (150, "Borderline High"),
    (170, "High"),
    (200, "Very High")])
def test_check_LDL(LDL_input, expected):
    from blood_calculator import check_LDL
    answer = check_LDL(LDL_input)
    assert answer == expected

@pytest.mark.parametrize("total_input, expected",
    [(85, "Normal"),
    (220, "Borderline High"),
    (250, "High")])
def test_check_total(total_input, expected):
    from blood_calculator import check_total
    answer = check_total(total_input)
    assert answer == expected

