import uvicorn
import os
from api.config import APP_PORT, APP_HOST, LOG_LEVEL

if __name__ == '__main__':
    uvicorn.run('api:api', host=APP_HOST, port=APP_PORT, log_level=LOG_LEVEL.lower())