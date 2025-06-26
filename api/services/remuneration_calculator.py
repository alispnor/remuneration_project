from decimal import Decimal
import logging

logger = logging.getLogger(__name__)


class RemunerationCalculator:
    @staticmethod
    def calculate_iss(value: Decimal) -> Decimal:
        return round(value * Decimal("0.02"), 5)

    @staticmethod
    def calculate_nf_value(value: Decimal, iss: Decimal, pis: Decimal, cofins: Decimal, csll: Decimal) -> Decimal:
        return round(value - (iss + pis + cofins + csll), 5)

    @staticmethod
    def validate_percent_value(value: Decimal, net_value: Decimal, percent_value: Decimal):
        if net_value == 0:
            return  # evita divisão por zero

        calculated_percent = round((value / net_value) * 100, 2)

        if abs(calculated_percent - percent_value) > Decimal("0.1"):
            logger.warning(
                f"Alerta: percent_value divergente! Esperado: {calculated_percent}, Informado: {percent_value}"
            )
