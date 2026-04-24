from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.db import init_db
from routes import register, login

app = FastAPI(
    title="Book Store API",
    version="1.0.0",
    openapi_version="3.0.3",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers with /auth prefix
app.include_router(register.router, prefix="/auth/api")
app.include_router(login.router, prefix="/auth/api")

# Startup
@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
async def root():
    return {"message": "Book Store API Running 🚀"}

# ALB health check
@app.get("/health")
def health():
    return {"status": "ok"}

# Optional API health check
@app.get("/auth/api/health")
async def api_health():
    return {"status": "ok"}
