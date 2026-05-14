from pymongo import MongoClient

# Conexión MongoDB local
client = MongoClient("mongodb://localhost:27017")

# Base de datos
db = client["robot_logs"]

# Colección
collection = db["events"]