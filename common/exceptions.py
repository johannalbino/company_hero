from rest_framework.exceptions import APIException
from http import HTTPStatus


class ParameterInvalid(APIException):
    status_code = 404
    default_code = 'service_unavailable'
    default_detail = (
        'Verifique os parâmetros enviados na requisição e tente novamente.'
    )


class CompanyNonexistent(APIException):
    status_code = HTTPStatus.OK.value
    default_code = HTTPStatus.OK.phrase
    default_detail = (
        'Não foi encontrado nenhuma empresa com os dados informados, verifique a empresa selecionada e tente novamente.'
    )
