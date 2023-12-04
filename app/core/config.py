import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.environ.get("APP_NAME", "life")
APP_ENV = os.environ.get("APP_ENV", "development")
SHOW_DOCS_ENVIRONMENT = [
    "development",
]

if APP_ENV in SHOW_DOCS_ENVIRONMENT:
    APP_CONFIGS = {
        "title": APP_NAME.replace("-", " ").title(),
        "openapi_url": "/openapi.json",
        "docs_url": "/docs",
        "description": "For Everything!",
    }
else:
    APP_CONFIGS = {}

AUTH_KEY = os.environ.get("AUTH_KEY", "dev")

CLEAN_USER = os.environ.get("CLEAN_USER", "")
CLEAN_PASS = os.environ.get("CLEAN_PASS", "")
LOGIN_PAGE = os.environ.get("LOGIN_PAGE", "")
HOME_PAGE = os.environ.get("HOME_PAGE", "")

API_KEY = os.environ.get("API_KEY", "")
USER_ID = os.environ.get("USER_ID", "")

SELENIUM_URL = os.getenv("SELENIUM_URL", "http://localhost:4444")
