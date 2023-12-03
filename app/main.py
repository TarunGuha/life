from fastapi import FastAPI
from core import APP_ENV, APP_CONFIGS, SHOW_DOCS_ENVIRONMENT

app = FastAPI(**APP_CONFIGS)

if APP_ENV not in SHOW_DOCS_ENVIRONMENT:
    from mangum import Mangum

    handler = Mangum(app)


@app.get("/")
def read_root():
    return {"message": f"Life Deployed Successfully! on {APP_ENV}"}
