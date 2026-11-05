import pytest
from self_storage import rent_due, access_allowed, payment_status


# RENT DUE TESTS

def test_invalid_unit_size():
    with pytest.raises(ValueError):
        rent_due("extra_large", 5, False, False)


def test_negative_months():
    with pytest.raises(ValueError):
        rent_due("small", -1, False, False)


def test_member_discount():
    assert rent_due("small", 3, False, True) == 80


def test_large_member_no_extra_coverage():
    assert rent_due("large", 4, False, True) == 80


def test_climate_controlled_rent():
    assert rent_due("small", 3, True, False) == 240


def test_normal_rent():
    assert rent_due("medium", 4, False, False) == 160


def test_long_term_rent_discount():
    assert rent_due("small", 8, False, False) == 490


def test_long_term_climate_rent_discount():
    assert rent_due("small", 8, True, False) == 735


# ACCESS ALLOWED TESTS

def test_owner_access_allowed():
    assert access_allowed(2, 4, True) is True


def test_owner_access_denied():
    assert access_allowed(12, 5, True) is False


def test_visitor_access_allowed():
    assert access_allowed(12, 2, False) is True


def test_visitor_exceeds_limit():
    assert access_allowed(12, 3, False) is False


def test_access_before_opening():
    assert access_allowed(5, 1, False) is False


def test_access_after_closing():
    assert access_allowed(23, 1, False) is False


# PAYMENT STATUS TESTS

def test_autopay_current():
    assert payment_status(5, True, False) == "current"
import pytest
from self_storage import rent_due, access_allowed, payment_status


# RENT DUE TESTS

def test_invalid_unit_size():
    with pytest.raises(ValueError):
        rent_due("extra_large", 5, False, False)


def test_negative_months():
    with pytest.raises(ValueError):
        rent_due("small", -1, False, False)


def test_member_discount():
    assert rent_due("small", 3, False, True) == 80


def test_large_member_no_extra_coverage():
    assert rent_due("large", 4, False, True) == 80


def test_climate_controlled_rent():
    assert rent_due("small", 3, True, False) == 240


def test_normal_rent():
    assert rent_due("medium", 4, False, False) == 160


def test_long_term_rent_discount():
    assert rent_due("small", 8, False, False) == 490


def test_long_term_climate_rent_discount():
    assert rent_due("small", 8, True, False) == 735


# ACCESS ALLOWED TESTS

def test_owner_access_allowed():
    assert access_allowed(2, 4, True) is True


def test_owner_access_denied():
    assert access_allowed(12, 5, True) is False


def test_visitor_access_allowed():
    assert access_allowed(12, 2, False) is True


def test_visitor_exceeds_limit():
    assert access_allowed(12, 3, False) is False


def test_access_before_opening():
    assert access_allowed(5, 1, False) is False


def test_access_after_closing():
    assert access_allowed(23, 1, False) is False


# PAYMENT STATUS TESTS

def test_autopay_current():
    assert payment_status(5, True, False) == "current"


def test_manual_payment_current():
    assert payment_status(5, False, False) == "current"


def test_payment_grace_period():
    assert payment_status(-5, True, False) == "grace"


def test_payment_lien():
    assert payment_status(-16, True, False) == "lien"


def test_prior_late_payment():
    assert payment_status(10, True, True) == "current"
