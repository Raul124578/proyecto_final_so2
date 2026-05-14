import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Cargar variables .env
load_dotenv()

# Leer variable de entorno
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://localhost:27017"
)

# Conexión MongoDB
client = MongoClient(MONGO_URI)

# Base de datos
db = client["robot_logs"]

# Colección
collection = db["events"]