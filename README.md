# Company HERO API

API para cadastrar empresas e funcionários para controle simples, onde o funcionário será o usuário da 
plataforma podendo o mesmo estar em uma ou mais empresas.

## Instruções

Para executar a API localmente é necessário que você clone o projeto em seu computador local.

## Pré-requisitos

```
python 3.7+
django 3.0+
django-rest-framework 3.11+
postgres 9+
```

## Instalação

Deve criar a database no postgres antes de executar os comandos de migração.

Nome do banco: company_hero

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Executando os testes

```
coverage run manage.py tests
```

## Documentação API
A API utiliza o framework [DRF-YASG](https://github.com/axnsan12/drf-yasg#installation) para documentação da API e seus
enpoints.

```
localhost:8000/api-docs
```

## URLS e Metódos
Abaixo é explicado todos as urls disponíveis e como realizar as requisições.

**Observação:** Para mais detalhes das requisições acesse o link do artigo acima.

##### Cadastro de empresas

POST
```
URL: http://localhost:8000/empresas/
JSON: {
	"name": "Nome da empresa",
	"fantasy_name": "Nome fantasia da Empresa",
	"cnpj": "00000000000000",
	"address": {
		"zip_code": "CEP",
		"address": "Logradouro",
		"neighborhood": "Bairro",
		"state": "Estado",
		"number": "Número",
		"complement": "Complemento"
	}
}
```

GET
```
URL: http://localhost:8000/empresas/
RETORNO: {
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "address": {
        "id": 1,
        "zip_code": "CEP",
        "address": "Logradouro",
        "neighborhood": "Bairro",
        "state": "Estado",
        "number": "Número",
        "complement": "Complemento"
      },
      "employees": [],
      "name": "Company Hero",
      "fantasy_name": "Company Hero",
      "cnpj": "00000000000000"
    }
  ]
}
```

DELETE
```
URL: http://localhost:8000/empresas/{id}/
RETORNO: {
    status_code: 204
}
```


##### Cadastro de funcionários/usuários

POST
```
URL: http://localhost:8000/funcionarios/
JSON: {
    "username": "Username Usuário",
    "name": "Nome Completo",
    "phone": "Telefone",
    "data_birth": "Data de Nascimento",
    "cpf": "Documento de id"
    "email": "Email do usuario",
		"company": [{
			"id": 1
		}, {
			"id": 2
		}],
    "address": {
			"zip_code": "CEP",
			"address": "Logradouro",
			"neighborhood": "Bairro",
			"state": "Estado",
			"number": "Número",
			"complement": "Complemento"
		}
    }
```

GET
```
URL: http://localhost:8000/funcionarios/
RETORNO: {
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 3,
      "address": {
        "id": 1,
        "zip_code": "CEP",
        "address": "Logradouro",
        "neighborhood": "Bairro",
        "state": "Estado",
        "number": "Número",
        "complement": "Complemento"
      },
      "company": [
        {
          "id": 1,
          "name": "Nomeda empresa",
          "fantasy_name": "Nome fantasia da empresa",
          "cnpj": "00000000000000"
        }
    ]
      "username": "Username",
      "name": "Nome Completo",
      "phone": "Telefone",
      "email": "Email do usuário",
      "data_birth": "Data de nascimento",
      "cpf": "Documento de ID"
    }
}
```

DELETE
```
URL: http://localhost:8000/funcionarios/{id}/
RETORNO: {
    status_code: 204
}
```

##### PAGINAÇÂO
Foi configurado 10 resultados por página, para fazer a paginação é só realizar a requisição incluindo ?page=2 ou +

Exemplo: 
```
URL: http://localhost:8000/funcionarios/?page=2
```