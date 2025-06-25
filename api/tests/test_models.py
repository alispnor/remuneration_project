import pytest
from api.models import UnitRemuneration
from decimal import Decimal
from datetime import date
import uuid

@pytest.mark.django_db
def test_unit_remuneration_calculation():
    instance = UnitRemuneration.objects.create(
        competence_date=date(2024, 7, 31),
        value=Decimal("100.00"),
        pis=Decimal("0.00"),
        cofins=Decimal("0.00"),
        csll=Decimal("0.00"),
        insured="JOÃO TESTE",
        policy="123456",
        endorsement="0",
        class_of_insurance="312",
        extract_number="20240731",
        apuration_statement_aggregated_id=1,
        unit_remuneration_status_id=1,
        installment=1,
        percent_value=Decimal("6.25"),
        date_of_export=date.today(),
        entries_date=None,
        net_value=Decimal("1600.00"),
        broker_insurance_company_uuid=uuid.uuid4(),
        ir=Decimal("0.00"),
        type_entry_id=None
    )
    assert instance.iss == Decimal("2.00000")
    assert instance.nf_value == Decimal("98.00000")

@pytest.mark.django_db
def test_percent_value_alert_log(caplog):
    with caplog.at_level("WARNING"):
        UnitRemuneration.objects.create(
            competence_date=date(2024, 7, 31),
            value=Decimal("100.00"),
            pis=Decimal("0.00"),
            cofins=Decimal("0.00"),
            csll=Decimal("0.00"),
            insured="MARIA ALERTA",
            policy="654321",
            endorsement="1",
            class_of_insurance="312",
            extract_number="20240731",
            apuration_statement_aggregated_id=2,
            unit_remuneration_status_id=1,
            installment=1,
            percent_value=Decimal("5.00"),
            date_of_export=date.today(),
            entries_date=None,
            net_value=Decimal("1600.00"),
            broker_insurance_company_uuid=uuid.uuid4(),
            ir=Decimal("0.00"),
            type_entry_id=None
        )
    assert any("percent_value divergente" in message for message in caplog.messages)

