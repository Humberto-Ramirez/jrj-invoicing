import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="JRJ Invoicing API",
    openapi_url="/app/v1/openapi.json"
)


@app.get("/")
async def root():
    return {"status": "Up!"}


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
