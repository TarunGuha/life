from fastapi import FastAPI
from mangum import Mangum
from core import APP_ENV, APP_CONFIGS

app = FastAPI(**APP_CONFIGS)
handler = Mangum(app)


@app.get("/")
def read_root():
    return {"message": f"Life Deployed Successfully! on {APP_ENV}"}
