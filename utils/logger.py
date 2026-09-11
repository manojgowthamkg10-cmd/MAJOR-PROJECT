import logging
import os
from logging.handlers import RotatingFileHandler

# Create logs directory if it doesn't exist
LOG_DIRECTORY = "logs"
os.makedirs(LOG_DIRECTORY, exist_ok=True)

# Log file path
LOG_FILE = os.path.join(LOG_DIRECTORY, "backend.log")

# Configure logger
logger = logging.getLogger("EarlyDetectionBackend")
logger.setLevel(logging.INFO)

# Prevent duplicate handlers
if not logger.handlers:

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)


def get_logger():
    """
    Returns configured application logger.
    """
    return logger