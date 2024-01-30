from fastapi import FastAPI
from core import APP_ENV, APP_CONFIGS, SHOW_DOCS_ENVIRONMENT
from api.endpoints.main_router import router as main_router

app = FastAPI(**APP_CONFIGS)

if APP_ENV not in SHOW_DOCS_ENVIRONMENT:
    from mangum import Mangum

    handler = Mangum(app)

app.include_router(main_router)
