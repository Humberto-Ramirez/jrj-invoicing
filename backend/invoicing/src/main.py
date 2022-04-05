import uvicorn

if __name__ == "__main__":
    uvicorn.run(app="jrj_invoicing.main:app", reload=True)
