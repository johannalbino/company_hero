EMPLOYEE_CREATE_PAYLOAD = {
    "username": "johannalbino",
    "name": "Johann Albino",
    "phone": "31995494755",
    "email": "johann@gmail.com",
    "date_birth": "1995-06-17",
    "cpf": "12345678912",
    "company": [{
        "id": 2
    }],
    "address": {
        "zip_code": "31970752",
        "address": "Rua Nilza Brito",
        "neighborhood": "Vitoria",
        "state": "MG",
        "number": "51",
        "complement": "Casa"
    }
}

EMPLOYEE_GET = {
  "count": 1,
  "next": None,
  "previous": None,
  "results": [
    {
      "id": 1,
      "address": {
        "zip_code": "30140000",
        "address": "Avenida Brasil",
        "neighborhood": "Santa Efigênia",
        "state": "MG",
        "number": "255",
        "complement": "Predio"
      },
      "company": [
        {
          "id": 1,
          "name": "Teste by Test",
          "fantasy_name": "Test",
          "cnpj": "01234567890123"
        }
      ],
      "username": "teste",
      "name": "Johann Albino",
      "phone": "31995494755",
      "email": "johann@gmail.com",
      "date_birth": "1995-06-17",
      "cpf": "13345678917"
    }
  ]
}
