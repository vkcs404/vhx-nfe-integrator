import requests
import json

# Configurações da API do VHSYS
API_VHSYS = "https://api.vhsys.com.br/v2/"
API_KEY = "sua_chave_de_api"  # Substitua pela sua chave de API

def emitir_nota_fiscal(dados_nota):
    """
    Emite uma nota fiscal utilizando a API do VHSYS.
    """
    url = f"{API_VHSYS}notas-fiscais"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(dados_nota))
        if response.status_code == 201:
            print("Nota fiscal emitida com sucesso!")
            return response.json()
        else:
            print(f"Erro ao emitir nota: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Erro na integração: {e}")

# Exemplo de dados para emitir nota
if __name__ == "__main__":
    dados_nota = {
        "cliente": {
            "nome": "João Silva",
            "cpf_cnpj": "12345678901",
            "endereco": "Rua das Flores, 123"
        },
        "produtos": [
            {
                "descricao": "Produto Exemplo",
                "quantidade": 2,
                "valor_unitario": 50.0
            }
        ],
        "valor_total": 100.0
    }
    emitir_nota_fiscal(dados_nota)
