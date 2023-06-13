import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from endpoints import user_router

app = FastAPI()
app.include_router(user_router)


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("main:app",
                host="localhost",
                port=8080,
                log_level="info",
                reload=True)
