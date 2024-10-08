from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import test_db_connection
from appv1.routers import users, roles, categories, login


app = FastAPI()
# Incluir routers

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(roles.router, prefix="/roles", tags=["Roles"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])
app.include_router(login.router, prefix="/access", tags=["Access"])

# Configuración de CORS para permitir todas las solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Permitir estos métodos HTTP
    allow_headers=["*"],  # Permitir cualquier encabezado en las solicitudes
)

@app.on_event("startup")
def on_startup():
    test_db_connection()

@app.get("/")
def read_root():
    return {
                "message": "Adso 2670586",
                "autor": "Juanpis Gonzales"
            }

