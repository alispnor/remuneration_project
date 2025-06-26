from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.conf import settings

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # Ambiente de produção (oculta detalhes)
        if not settings.DEBUG:
            # Se for erro de validação, também esconde a resposta
            if isinstance(exc, ValidationError):
                return Response(
                    {'detail': 'Erro de validação. Verifique os campos obrigatórios.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            # Qualquer outro erro tratado
            return Response(
                {'detail': 'Erro interno. Contate o suporte.'},
                status=response.status_code
            )
        else:
            # Em desenvolvimento, retorna o erro padrão completo (útil para debug)
            return response

    # Erro inesperado (não tratado pelo DRF)
    return Response(
        {'detail': 'Erro desconhecido. Tente novamente mais tarde.'},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
