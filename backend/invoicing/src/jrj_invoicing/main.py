from fastapi import FastAPI
from jrj_invoicing.api import api

app = FastAPI(
    title="JRJ Invoicing API",
    openapi_url="/app/v1/openapi.json"
)
app.include_router(api.api_router)


@app.get("/")
async def root():
    return {"status": "Up!"}
