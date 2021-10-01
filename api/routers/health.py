from fastapi import APIRouter
from ..schemas.health import HealthStatus


health_router = APIRouter()


@health_router.get('/health')
def health_check() -> HealthStatus:
    return HealthStatus()
