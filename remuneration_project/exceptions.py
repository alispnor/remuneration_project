from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # Exibir apenas o erro genérico no Swagger e testes
        return Response({'detail': 'Erro interno. Contate o suporte.'}, status=response.status_code)

    # Erro inesperado (ex: 500)
    return Response({'detail': 'Erro desconhecido. Tente novamente mais tarde.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
