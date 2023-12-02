from fastapi import FastAPI
from core import APP_CONFIGS
from mangum import Mangum

app = FastAPI(**APP_CONFIGS)
handler = Mangum(app)


@app.get("/")
def read_root():
    return {"message": "Life Deployed Successfully!"}
