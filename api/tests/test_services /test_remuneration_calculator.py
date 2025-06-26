
import pytest
from decimal import Decimal
from api.services.remuneration_calculator import RemunerationCalculator


def test_calculate_iss():
    value = Decimal("100.00")
    iss = RemunerationCalculator.calculate_iss(value)
    assert iss == Decimal("2.00000")


def test_calculate_nf_value():
    value = Decimal("100.00")
    iss = Decimal("2.00")
    pis = Decimal("1.00")
    cofins = Decimal("1.00")
    csll = Decimal("1.00")

    nf_value = RemunerationCalculator.calculate_nf_value(value, iss, pis, cofins, csll)
    assert nf_value == Decimal("95.00")


def test_validate_percent_value_no_warning(caplog):
    value = Decimal("100.00")
    net_value = Decimal("1600.00")
    percent_value = Decimal("6.25")  # 100 / 1600 * 100 = 6.25

    with caplog.at_level("WARNING"):
        RemunerationCalculator.validate_percent_value(value, net_value, percent_value)

    assert "percent_value divergente" not in caplog.text


def test_validate_percent_value_with_warning(caplog):
    value = Decimal("100.00")
    net_value = Decimal("1600.00")
    percent_value = Decimal("5.00")  # < 6.25, diferença > 0.1

    with caplog.at_level("WARNING"):
        RemunerationCalculator.validate_percent_value(value, net_value, percent_value)

    assert "percent_value divergente" in caplog.text
