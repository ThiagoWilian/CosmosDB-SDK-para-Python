# Importando as bibliotecas necessárias
from azure.cosmos import CosmosClient
import urllib3
from config import database

# Desabilita as notificações de segurança (certificados SSL/TLS)
urllib3.disable_warnings()

# Lê as credenciais de acesso do arquivo config.py
endpoint = database.credenciais['endpoint']
key = database.credenciais['key']

# Inicializa o cliente Cosmos DB usando as credenciais fornecidas
client = CosmosClient(endpoint, key)

# Imprime a lista de bancos de dados disponíveis no Cosmos DB
print("========= Listagem dos bancos de dados =========")
for db in client.list_databases():
    print(f"\nBanco de dados -> {db['id']}")

# Imprime a lista de containers disponíveis em um banco de dados específico
print("\n\n========= Listagem dos containers =========")
database_name = 'BancoTeste'
databases = client.get_database_client(database_name)

for container in databases.list_containers():
    print(f"\nContainer -> {container['id']}")
