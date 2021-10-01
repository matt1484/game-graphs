import structlog
import logging
from .config import LOG_LEVEL
import sys
import datetime

logging.basicConfig(stream=sys.stdout, format='%(message)s')
logger = logging.getLogger('app')
logger.setLevel(logging._nameToLevel.get(LOG_LEVEL, logging.INFO))
logger = structlog.wrap_logger(logger, wrapper_class=structlog.BoundLogger)