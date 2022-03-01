from fastapi import FastAPI

app = FastAPI()


@app.post("/diia-reciver")
async def diia_reciver(data):
    print(data)
    return { "success": True }
