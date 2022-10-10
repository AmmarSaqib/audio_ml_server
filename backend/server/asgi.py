"""
Author: Ammar Saqib
Main file to trigger the Uvicorn server
"""

import os
import uvicorn
import logging
from app.main import app


if __name__ == "__main__":
    logging.info(os.environ.get("APP_PORT"))
    uvicorn.run(app, host="0.0.0.0", port=os.environ.get("APP_PORT"))