# Importando as bibliotecas necessárias
from azure.cosmos import CosmosClient
import urllib3
from config import database

# Desabilita as notificações de segurança (certificados SSL/TLS)
urllib3.disable_warnings()

# Lê as credenciais de acesso do arquivo config.py
endpoint = database.credenciais['endpoint']
key = database.credenciais['key']

# Função para excluir vários containers de um banco de dados específico
def delete_varios_containers(client, database_id, container_ids):
    # Obtém o cliente do banco de dados
    database = client.get_database_client(database_id)

    # Itera sobre os IDs dos containers e tenta excluí-los
    for container_id in container_ids:
        try:
            database.delete_container(container_id)
            print(f"Contêiner '{container_id}' excluído com sucesso.")
        except Exception as e:
            print(f"\nErro ao excluir o contêiner '{container_id}'")
            print(f"Tipo de erro: {type(e).__name__}\n")

# Inicializa o cliente Cosmos DB usando as credenciais fornecidas
client = CosmosClient(endpoint, key)

# Define o ID do banco de dados e a lista de IDs dos containers que deseja excluir
database_id = "BancoTeste"
container_ids = ['Azure App Service', 'Functions', 'Azure Databricks', 'Storage', 'Azure Cosmos DB']

# Chama a função para excluir os containers especificados
delete_varios_containers(client, database_id, container_ids)
