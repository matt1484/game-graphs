import os
from dotenv import load_dotenv

def get_var(var_name: str, dtype: type = str, default = None):
    var = os.getenv(var_name, default)
    # bools need to be handled differently
    if dtype == bool:
        return (var or '').lower() in ['true', 'yes', 'y', '1']
    try:
        return dtype(var)
    except:
        if default == ...: # simple way to require var
            raise
        return default

# load .env files which will load based on order (assuming direct env vars have higher priority)
env_files = get_var('ENV_FILES', default='.env').split(',')
for path in env_files:
    if path and os.path.exists(path):
        load_dotenv(path, override=False)


# APP args (uvicorn)
APP_PORT = get_var('APP_PORT', int)
APP_HOST = get_var('APP_HOST')

# LOG args
LOG_LEVEL = get_var('LOG_LEVEL').upper()

# POSTGRES args (SQLAlchemy)
POSTGRES_DB = get_var('POSTGRES_DB')
POSTGRES_HOST = get_var('POSTGRES_HOST', default=...)
POSTGRES_PORT = get_var('POSTGRES_PORT', int)
POSTGRES_USER = get_var('POSTGRES_USER')
POSTGRES_PASSWORD = get_var('POSTGRES_PASSWORD', default=...)