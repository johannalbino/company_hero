COMPANY_CREATE_PAYLOAD = {
    "name": "Johann Albino LTDA",
    "fantasy_name": "Johann",
    "cnpj": "00000000000000",
    "address": {
        "zip_code": "30140000",
        "address": "Avenida Brasil",
        "neighborhood": "Santa Efigenia",
        "state": "MG",
        "number": "141",
        "complement": "Prédio"
    }
}

COMPANY_GET = {
    'count': 1,
    'next': None,
    'previous': None,
    'results': [{
        'address': {
            'address': 'Avenida Brasil',
            'complement': 'Predio',
            'neighborhood': 'Santa Efigênia',
            'number': '255',
            'state': 'MG',
            'zip_code': '30140000'
        },
        'cnpj': '01234567890123',
        'employees': [],
        'fantasy_name': 'Test',
        'name': 'Teste by Test'
    }]
}
