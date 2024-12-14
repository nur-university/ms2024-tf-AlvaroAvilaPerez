from fastapi import FastAPI
from api_d_p.controllers.delivery_person_routes import router as delivery_person_router
from api_d_p.controllers.package_routes import router as package_router
from api_d_p.controllers.delivery_routes import router as delivery_router
from contextlib import asynccontextmanager
from Infrastructure.data_base.data_base import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Inicializa la base de datos al iniciar la aplicación."""
    init_db()  # Inicializa la base de datos
    yield  # Esto permite que la aplicación funcione
    # Aquí puedes agregar cualquier limpieza que necesites al cerrar la aplicación

# Crear la aplicación con el ciclo de vida definido
app = FastAPI(lifespan=lifespan)

# Incluye las rutas para los repartidores
app.include_router(delivery_person_router, prefix="/delivery_person", tags=["Delivery Person"])

# Incluye las rutas para los paquetes
app.include_router(package_router, prefix="/packages", tags=["Packages"])

# Incluye las rutas para las entregas
app.include_router(delivery_router, prefix="/deliveries", tags=["Deliveries"])
