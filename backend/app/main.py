from fastapi import FastAPI

app = FastAPI()
from fastapi import FastAPI

app = FastAPI()

# Simulación de base de datos
eventos = []

# Ruta principal
@app.get("/")
def home():
    return {"mensaje": "Backend funcionando"}

# Obtener eventos
@app.get("/events")
def get_events():
    return {"eventos": eventos}

# Crear evento
@app.post("/event")
def create_event(evento: dict):

    eventos.append(evento)

    return {
        "mensaje": "Evento agregado",
        "evento": evento
    }