import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from api.models import UnitRemuneration
from decimal import Decimal
from datetime import date
import uuid

@pytest.mark.django_db
def test_create_unit_remuneration():
    client = APIClient()
    url = reverse('unitremuneration-list')
    payload = {
        "competence_date": "2024-07-31",
        "value": "100.00",
        "pis": "0.00",
        "cofins": "0.00",
        "csll": "0.00",
        "insured": "JOÃO TESTE",
        "policy": "123456",
        "endorsement": "0",
        "class_of_insurance": "312",
        "extract_number": "20240731",
        "apuration_statement_aggregated_id": 1,
        "unit_remuneration_status_id": 1,
        "installment": 1,
        "percent_value": "6.25",
        "date_of_export": str(date.today()),
        "entries_date": None,
        "net_value": "1600.00",
        "broker_insurance_company_uuid": str(uuid.uuid4()),
        "ir": "0.00",
        "type_entry_id": None
    }
    response = client.post(url, payload, format='json')
    assert response.status_code == 201
    assert UnitRemuneration.objects.count() == 1
