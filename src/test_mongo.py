from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

client = MongoClient(
    "mongodb+srv://<USUARIO>:<PASS>@ac-pxpxh1v-shard-00-00.jhtphd8.mongodb.net/tuDB?retryWrites=true&w=majority",
    serverSelectionTimeoutMS=5000,
    tls=True
)

try:
    info = client.server_info()
    print("🟢 Conexión exitosa. Versión de MongoDB:", info.get("version"))
except ServerSelectionTimeoutError as e:
    print("🔴 FALLO la conexión:", e)
