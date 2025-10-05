import logging
from pathlib import Path

# Configure logger
logging.basicConfig(
    level=logging.INFO,  # Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    handlers=[logging.StreamHandler()]                   # Log to console
)

# Create a global logger
logger = logging.getLogger("ETL-Pipeline")
