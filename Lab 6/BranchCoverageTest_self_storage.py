from self_storage import rent_due, access_allowed, payment_status


# RENT DUE BRANCH TESTS
def test_unknown_unit():
    try:
        rent_due("extra_large", 2, False, False)
        assert False
    except ValueError:
        assert True


def test_negative_months():
    try:
        rent_due("small", -1, False, False)
        assert False
    except ValueError:
        assert True


def test_member_small_unit():
    assert rent_due("small", 3, False, True) == 80


def test_large_unit_member_no_extra_coverage():
    assert rent_due("large", 5, False, True) == 160


def test_no_extra_rent():
    assert rent_due("small", 1, False, False) == 0


def test_climate_rate():
    assert rent_due("small", 3, True, False) == 240


def test_non_climate_rate():
    assert rent_due("small", 3, False, False) == 160


def test_long_term_non_climate():
    assert rent_due("small", 9, False, False) == 560


def test_long_term_climate():
    assert rent_due("small", 9, True, False) == 840


# ACCESS CONTROL BRANCH TESTS
def test_owner_allowed():
    assert access_allowed(12, 4, True) is True


def test_owner_too_many_visitors():
    assert access_allowed(12, 5, True) is False


def test_non_owner_before_opening():
    assert access_allowed(5, 1, False) is False


def test_non_owner_after_closing():
    assert access_allowed(23, 1, False) is False


def test_non_owner_allowed():
    assert access_allowed(12, 2, False) is True


def test_non_owner_too_many_visitors():
    assert access_allowed(12, 3, False) is False


# PAYMENT STATUS BRANCH TESTS
def test_autopay_cutoff():
    assert payment_status(0, True, False) == "current"


def test_manual_payment_cutoff():
    assert payment_status(5, False, False) == "current"


def test_prior_late_payment_cutoff():
    assert payment_status(15, True, True) == "current"


def test_payment_grace():
    assert payment_status(-1, True, False) == "grace"


def test_payment_lien():
    assert payment_status(-16, True, False) == "lien"
