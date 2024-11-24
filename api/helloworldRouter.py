from fastapi import FastAPI

#instance object

app = FastAPI

@app.get("/api/sayhello")
async def sayhello():
    return{"Hello world - First GET"}