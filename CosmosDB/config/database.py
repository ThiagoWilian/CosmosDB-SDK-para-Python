import os
from dotenv import load_dotenv

load_dotenv()

credenciais = {
    'endpoint': os.environ['ENDPOINT'],
    'key': os.environ['KEY']

}
