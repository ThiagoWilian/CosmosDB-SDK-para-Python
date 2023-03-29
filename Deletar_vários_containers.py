from azure.cosmos import CosmosClient
import urllib3

from config import database


# Desabilita as notificações de segurança
urllib3.disable_warnings() 

endpoint = database.credenciais['endpoint']
key = database.credenciais['key']

def delete_varios_containers(client, database_id, container_ids):
    database = client.get_database_client(database_id)
    
    for container_id in container_ids:
        try:
            database.delete_container(container_id)
            print(f"Contêiner '{container_id}' excluído com sucesso.")
        except Exception as e:
            print(f"\nErro ao excluir o contêiner '{container_id}'")
            print(f"Tipo de erro: {type(e).__name__}\n")


client = CosmosClient(endpoint, key)
database_id = "BancoTeste"
container_ids = ['Azure App Service', 'Functions', 'Azure Databricks', 'Storage','Azure Cosmos DB']


delete_varios_containers(client, database_id, container_ids)