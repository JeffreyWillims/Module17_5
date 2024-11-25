from fastapi import FastAPI
from routers import task, user
import asyncio
import uvicorn

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)


if __name__ == "__main__":
    asyncio.run(uvicorn.run(app, host="127.0.0.1", port=8000, loop="asyncio"))