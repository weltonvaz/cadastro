import requests

country_uf = {
        'RO': 'Rondônia',
        'AC': 'Acre',
        'AM': 'Amazonas',
        'RR': 'Roraima',
        'PA': 'Pará',
        'AP': 'Amapá',
        'TO': 'Tocantins',
        'MA': 'Maranhão',
        'PI': 'Piauí',
        'CE': 'Ceará',
        'RN': 'Rio Grande do Norte',
        'PB': 'Paraíba',
        'PE': 'Pernambuco',
        'AL': 'Alagoas',
        'SE': 'Sergipe',
        'BA': 'Bahia',
        'MG': 'Minas Gerais',
        'ES': 'Espírito Santo',
        'RJ': 'Rio de Janeiro',
        'SP': 'São Paulo',
        'PR': 'Paraná',
        'SC': 'Santa Catarina',
        'RS': 'Rio Grande do Sul',
        'MS': 'Mato Grosso do Sul',
        'MT': 'Mato Grosso',
        'GO': 'Goiás',
        'DF': 'Distrito Federal'
    }


def is_valid(inputted):
    """
    Essa função irá verificar o QueryDict trago pelo método POST do nosso frontend e fazer uma verificação dos campos an
    tes de persistir os dados no banco de dados.
    :param inputted: Query Dict trago pelo POST
    :return: Um valor booleano
    """
    for key in inputted.keys():

        if key != 'complemento':
            if inputted.get(key) is None:
                return False
            elif len(inputted.get(key)) == 0:
                return False
            else:
                pass

        if key == 'estado':
            if inputted.get(key) not in country_uf.values():
                return False
            else:
                pass

        if key == 'cep':
            if len(inputted.get(key)) != 8:
                return False
            else:
                cep = inputted.get(key)
                try:
                    int(cep)
                except (TypeError, ValueError):
                    return False
                else:
                    url = f"https://viacep.com.br/ws/{cep}/json/"
                    response = requests.get(url)
                    response = response.json()
                    if 'erro' in response.keys():
                        return False
    return True
