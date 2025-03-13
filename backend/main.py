from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.visitas import router as visitas_router

# Initializes  FastAPI app
app = FastAPI()

# List of alllowed origins
origins = [
    "http://localhost:5500",
    "http://128.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all HTTP methods (GET, POST, PUT...)
    allow_headers=["*"], # Allows all headers
)

app.include_router(visitas_router)

# Route to the home page
@app.get("/")
def home():
    return {"mensaje": "mensaje enviado desde la api"}
